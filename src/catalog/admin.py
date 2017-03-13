from django.contrib import admin

# Register your models here.
from .models import Category, Products

class CategoryAdmin(admin.ModelAdmin):
    #model = Category
    list_display = ['id', 'name']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Products)