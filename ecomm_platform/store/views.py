from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import View

from .models import Category, Promo


class BaseView(View):
    category_model = Category.objects.all()
    context = {
        'category_model': category_model,
    }


class Home(BaseView):
    template = loader.get_template('store/home.html')
    slider_model = Promo.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        self.context['slider_model'] = self.slider_model
        return HttpResponse(self.template.render(self.context, request))
