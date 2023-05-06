from django.contrib import admin
from cart import models


@admin.register(models.Cart)
class Cart(admin.ModelAdmin):
    search_fields = ('user', 'created')


@admin.register(models.CustomUser)
class CustomUser(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name')
