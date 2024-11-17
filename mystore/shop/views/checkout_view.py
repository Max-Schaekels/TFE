from django.shortcuts import render, redirect, get_object_or_404
from shop.services.cart_service import CartService


def index(request):
    cart = CartService.get_cart_details(request)
    return render(request, 'shop/checkout.html', {'cart' : cart})