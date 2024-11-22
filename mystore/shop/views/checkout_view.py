from django.shortcuts import render, redirect,get_object_or_404
from shop.services.cart_service import CartService
from shop.models.Carrier import Carrier
from shop.forms.CheckoutAddressForm import CheckoutAddressForm
from django.contrib import messages
from accounts.forms.CustomLoginForm import CustomLoginForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from accounts.models.Customer import Customer
from django.contrib.auth.hashers import make_password
import random
import string


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

def add_address(request):
    user = request.user
    
    #Vérification de la méthode
    if request.method == 'POST' :
        #Récupération du formulaire
        address_form = CheckoutAddressForm(request.POST)
        #Vérification de la validité
        if address_form.is_valid():
            address = address_form.save(commit=False) #sauvegarde sans envois en base de donné
            address.author = user #Association de l'user à author
            address.save()
            messages.success(request, 'Adresse correctement ajoutée.')


    return redirect('shop:checkout')


#On utilise JSON car cela fournit des informations similaire à un dictionnaire python utilisable en javascript car on veut pour la fonction que cela s'éxécute en arrière plan du site.

def login_form(request):
    #Vérification si l'utilisateur est déjà connecter
    if request.user.is_authenticated:
        return JsonResponse({"isSuccess": True, 'message': 'Cet utilisateur est déjà connecte'})

    #Vérification de la méthode
    if request.method == "POST":
        #Récupération de information de l'utilisateur
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        #Vérification qu'on a bien l'user et si oui on le connecte
        if user is not None:
            login(request, user)
            return JsonResponse({"isSuccess": True, 'message': 'Cet utilisateur est connecte'})
        else:
            return JsonResponse({"isSuccess": False, 'message': 'Information erronee. Impossible de se connecter'})

    return JsonResponse({"isSuccess": False, 'message': 'Erreur, requête non-valide'})

