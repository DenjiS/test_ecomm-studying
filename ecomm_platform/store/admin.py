from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline

from .models import Image, Tag, Category, Product


class ImagesInline(GenericStackedInline):  # stacked
    model = Image


class TagsInline(GenericTabularInline):  # tabular
    model = Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ImagesInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'name')
    list_filter = ('category__name',)
    inlines = [ImagesInline, TagsInline, ]
