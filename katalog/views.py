from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    catalog_items_data = CatalogItem.objects.all()
    context = {
        'items_list': catalog_items_data,
        'name': 'Syadza Nayla Arrana Desvianto',
        'student_id': '2106634055'
    }
    return render(request, "katalog.html", context)