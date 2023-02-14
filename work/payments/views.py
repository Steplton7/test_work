from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Item

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'item': item,
    }
    return render(request, 'home.html', context)
