from django.contrib import admin
from .models import Item
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name', 'description',)
    list_filter = ('name','price')

admin.site.register(Item, ItemAdmin)