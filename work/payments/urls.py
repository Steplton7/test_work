from django.urls import path
from django.views.decorators.cache import cache_page
from . import views


urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item'),

]
