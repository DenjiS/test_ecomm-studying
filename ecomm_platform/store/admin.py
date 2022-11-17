from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline

from .models import Image, Category, Product, Promo


class ImagesInline(GenericStackedInline):  # stacked
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'name', 'description')
    inlines = [ImagesInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('slug', 'price', 'name')
    list_filter = ('category__name',)
    inlines = [ImagesInline, ]


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ImagesInline, ]
