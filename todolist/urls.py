from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path('', show_my_todolist, name='show_my_todolist'),
    path('json/', todolist_json, name='todolist_json'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('complete-task/<int:pk>/', complete_task, name='complete_task'),
    path('delete-task/<int:pk>/', delete_task, name='delete_task'),
]