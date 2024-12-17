from django.shortcuts import get_object_or_404, render, redirect
import stripe.error
from shop.models.Order import Order
from django.http import JsonResponse
import stripe
from shop.services.payment_service import StripeService
from shop.services.cart_service import CartService

def index(request, order_id):
    payment_service = StripeService()
    stripe.api_key = payment_service.get_private_key()
    try:
        #récupération de la commande
        order = get_object_or_404(Order, id=order_id)
        #récupération du montant de la commande
        amount = int(order.order_cost_ttc *100)
        # Création d'une intention de payement avec les infos de la commande
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        #sauvegarde de l'intention de payement
        order.stripe_payment_intent = payment_intent['id']
        order.save()
        return JsonResponse({
            'clientSecret': payment_intent['client_secret'],
        })
    except Exception as e:
        return JsonResponse({"error": str(e) })
    

def payment_success(request):
    payment_intent_id = request.GET.get('payment_intent')

    if not payment_intent_id:
        print('Le paramètre payment_intent_client_secret est manquant')
        return redirect('shop:home')




    #vérification que la commande est bien payé : 
    try:
        payment_service = StripeService()
        stripe.api_key = payment_service.get_private_key()
        payment = stripe.PaymentIntent.retrieve(payment_intent_id)

        if payment.status == 'succeeded':
            #récupération de la commande sur base du stripe payment intent
            order = get_object_or_404(Order, stripe_payment_intent=payment_intent_id)
            order.is_paid = True
            order.save()
            CartService.clear_cart(request)
            print('Paiement réussi')
            return render (request, 'shop/payment_success.html' , {})
        else :
            print(f'Etat du paiement non réussi : {payment.status}')
            return redirect ('shop:home')
    except stripe.error.StripeError as e:
        print(f'Erreur strip : {str(e)}')

    except Exception as e:
        print(f'Une erreure s est produite :  {str(e)}')

        return redirect ('shop:home')

    
