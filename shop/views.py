from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from cart.forms import CartAddProductForm
from .models import Product, Category
from .forms import ReviewForm


class ProductsView(ListView):
    """Список товаров"""
    model = Product
    queryset = Product.objects.filter(available=True)


class ProductDetailView(DetailView):
    """Полное описание товара"""
    model = Product
    slug_field = "url"

    def get_context_data(self, *args, **kwargs):
        contest = super().get_context_data(*args, **kwargs)
        contest["cart_product_form"] = CartAddProductForm()
        return contest


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.product = product
            form.save()
        return redirect(product.get_absolute_url())
