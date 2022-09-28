# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import *

app_name = 'mywatchlist'

urlpatterns = [
    
    path('', show_watchlist, name='show_watchlist'),
    path('<str:type>/', show_all, name='show_all'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_xml_by_id, name='show_xml_by_id'),
]
