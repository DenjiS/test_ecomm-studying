from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Category


def home(request):  # TODO: parent class view, category model on every page
    category_model = Category.objects.all()
    template = loader.get_template('store/home.html')
    context = {
        'category_model': category_model
    }
    return HttpResponse(template.render(context, request))
