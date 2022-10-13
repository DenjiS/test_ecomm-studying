from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline, GenericTabularInline

from .models import Image, Tag, Category, Product, Promo


class ImagesInline(GenericStackedInline):  # stacked
    model = Image


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('word', 'url')

    def has_module_permission(self, request):
        return False


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ImagesInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'name')
    list_filter = ('category__name',)
    inlines = [ImagesInline, ]


@admin.register(Promo)
class PromoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [ImagesInline, ]
