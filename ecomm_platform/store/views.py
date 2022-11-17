from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import ListView

from .models import Category, Promo, Product, Image


class StoreBaseView(View):
    category_model = Category.objects.all()
    context = {
        'category_model': category_model
    }


class HomeView(StoreBaseView):
    template = loader.get_template('store/home.html')
    slider_model = Promo.objects.filter(active=True)

    def get(self, request, *args, **kwargs):
        self.context['slider_model'] = self.slider_model
        return HttpResponse(self.template.render(self.context, request))


class CatalogView(StoreBaseView, ListView):
    paginate_by = 16
    template_name = 'store/catalog.html'

    def get_queryset(self):
        self.category = get_object_or_404(
            Category,
            slug=self.kwargs['category_slug']
        )
        self.images = Image.objects.filter(
            default=True
        )
        return Product.objects.filter(
            category__slug=self.category.slug
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= self.context
        context['category'] = self.category
        context['product_images'] = self.images
        return context
