from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, pk):
    """Добавление товара в корзину"""
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, pk):
    """Удаление товара из корзины"""
    cart = Cart(request)
    product = Product.objects.get(id=pk)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})
