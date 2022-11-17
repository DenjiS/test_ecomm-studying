from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('<str:category_slug>/', views.CatalogView.as_view(), name='product_list_by_category',),
]