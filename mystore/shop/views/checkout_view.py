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

    #Récupération de new shipping address via la barre d'adresse
    new_shipping_address = request.GET.get('new_shipping_address', '')

    #Récupération du billing id via la barre d'adresse
    address_billing_id = request.GET.get('address_billing_id', '')

    #On regarde si billing id existe et si oui on transformer en entier 
    if address_billing_id and address_billing_id != "" :
        address_billing_id = int(address_billing_id)

    #Récupération du shipping id via la barre d'adresse
    address_shipping_id = request.GET.get('address_shipping_id', address_billing_id)

    #On regarde si shipping id existe et si oui on transformer en entier 
    if address_shipping_id and address_shipping_id != "" :
        address_shipping_id = int(address_shipping_id)

    #Variable pour voir si l'utilisateur est prêt ) payer
    ready_to_pay = False


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
    login_form = CustomLoginForm()
    return render(request, 'shop/checkout.html', {
        'cart' : cart, 
        'carriers' : carriers,
        'address_form' : address_form,
        'login_form' : login_form,
        'ready_to_pay' : ready_to_pay,
        'address_billing_id' : address_billing_id,
        'address_shipping_id' : address_shipping_id,
        'new_shipping_address' : new_shipping_address,
        })

def add_address(request):
    user = request.user
    
    #Vérification de la méthode
    if request.method == 'POST' :
        #Récupération du formulaire
        address_form = CheckoutAddressForm(request.POST)
        if not user.is_authenticated:
            #On récupère l'email dans la requete
            email = request.POST.get('email')
            #On vérifie si l'email existe déjà en base de donnée
            existing_user = Customer.objects.filter(email=email)

            if existing_user:
                login(request, existing_user)
                user = existing_user

            else:
                new_user = Customer()
                new_user.username = email
                new_user.email = email
                #génération d'un mdp aléatoire en string avec caractère ascii et des nombres
                password = ''.join(random.choices(string.ascii_letters+string.digits,k=8))
                #hashage du password (cryptage)
                new_user.password = make_password(password)
                
                # A faire : Envoi de mail de création de compte, contenant le mot de passe

                new_user.save()
                login(request, new_user)
                user = new_user



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

