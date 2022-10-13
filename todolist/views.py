from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from todolist.models import *

# Create your views here.
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_my_todolist"))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    return response

@login_required(login_url='/todolist/login/')
def show_my_todolist(request):
    my_todolist = Task.objects.filter(user=request.user).order_by('is_finished')
    form = CreateTask()
    
    context = {
        'my_todolist': my_todolist,
        'form' : form,
    }
    return render(request, "todolist.html", context)

def todolist_json(request):
    todolist = Task.objects.filter(user=request.user).order_by('is_finished')
    return JsonResponse(list(todolist.values()), safe=False)

def add_task(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")

        new_task = Task(user=user, title=title, description=description)
        new_task.save()

        return HttpResponse(b"CREATED", status=201)
    
    return HttpResponseNotFound()

def create_task(request):
    form = CreateTask()

    if request.method == "POST":
        form = CreateTask(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('todolist:show_my_todolist')
    
    context = {'form':form}
    return render(request, 'new_task.html', context)

def complete_task(request, pk):
    completed_task = Task.objects.get(pk=pk)
    completed_task.is_finished = not (completed_task.is_finished)
    completed_task.save()

    return redirect('todolist:show_my_todolist')

def delete_task(request, pk):
    completed_task = Task.objects.get(pk=pk)
    completed_task.delete()

    return redirect('todolist:show_my_todolist')