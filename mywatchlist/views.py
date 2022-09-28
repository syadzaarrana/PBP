from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from mywatchlist.models import MyWatchList

# Create your views here.
def show_watchlist(request):
    watchlist_data = MyWatchList.objects.all()
    context = {
        'watchlist': watchlist_data,
        'name': 'Syadza Nayla Arrana Desvianto',
        'student_id': '2106634055'
    }
    
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_all(request, type):
    data = MyWatchList.objects.all()

    print(request)
    print(type)

    if (type == "xml"):
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    
    if (type == "json"):
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
    return show_watchlist(request)