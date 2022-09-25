from django.contrib import admin
from .models import ImageAlbum, Image, Category, Product


class ImageInLine(admin.StackedInline):
    model = Image


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, ]


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('article_name', 'price', 'name')
