from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Image, Category, Product


class ImageInLine(GenericStackedInline):
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ImageInLine, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'name')
    list_filter = ('category__name',)
    inlines = [ImageInLine, ]
