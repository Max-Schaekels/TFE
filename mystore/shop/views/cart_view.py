from django.shortcuts import render, redirect, get_object_or_404
from shop.models.Product import Product
from shop.services.cart_service import CartService


def index(request):
    cart = CartService.get_cart_details(request)
     #vérifier si il y a quelque chose dans le panier sinon rediriger vers page home
    if not len(cart['items']):
        return redirect('shop:home')
    return render(request, 'shop/cart.html', {'cart': cart})


def add_to_cart(request, product_id):
    CartService.add_to_cart(request, product_id, 1)
    return redirect('shop:cart')


def remove_from_cart(request, product_id, quantity=1):
    CartService.remove_from_cart(request, product_id, quantity)
    return redirect('shop:cart')
