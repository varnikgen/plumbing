from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Product


class ProductsView(ListView):
    """Список товаров"""
    model = Product
    queryset = Product.objects.filter(available=True)


class ProductDetailView(DetailView):
    """Полное описание товара"""
    model = Product
    slug_field = "url"
