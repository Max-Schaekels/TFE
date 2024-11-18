from django.shortcuts import render, redirect, get_object_or_404
from shop.services.cart_service import CartService
from shop.models.Carrier import Carrier
from shop.forms.CheckoutAddressForm import CheckoutAddressForm


def index(request):
    #Récupération du carrier id via la barre d'adresse
    carrier_id = request.GET.get('carrier_id')
    if carrier_id and carrier_id != '':
        carrier = Carrier.objects.filter(id=carrier_id).first()
        if carrier :
            request.session['carrier'] = {
                'id' : carrier.id,
                'name' : carrier.name,
                'price' : carrier.price,
            }

    cart = CartService.get_cart_details(request)
    carriers = Carrier.objects.all()
    address_form = CheckoutAddressForm()
    return render(request, 'shop/checkout.html', {
        'cart' : cart, 
        'carriers' : carriers,
        'address_form' : address_form,
        })