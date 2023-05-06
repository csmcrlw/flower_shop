from django.contrib import admin
from shop import models


@admin.register(models.Product)
class Product(admin.ModelAdmin):
    search_field = ('name', 'category__name')
    list_display = ['name', 'slug', 'price', 'stock', 'available']
    list_filter = ('available', )
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Category)
class Category(admin.ModelAdmin):
    search_field = ('name',)
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
