from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Product


def catalog(request):
    product_model = Product.objects.all()
    template = loader.get_template('store/index.html')
    context = {
        'product_model': product_model
    }
    return HttpResponse(template.render(context, request))