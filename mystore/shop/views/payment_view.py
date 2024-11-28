from django.shortcuts import get_object_or_404, render
from shop.models.Order import Order
from django.http import JsonResponse
import stripe
from shop.services.payment_service import StripeService

def index(request, order_id):
    payment_service = StripeService()
    stripe.api_key = payment_service.get_private_key()
    try:
        #récupération de la commande
        order = get_object_or_404(Order, id=order_id)
        #récupération du montant de la commande
        amount = int(order.order_cost_ttc *100)
        # Création d'une intention de payement avec les infos de la commande
        intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='eur',
            # In the latest version of the API, specifying the `automatic_payment_methods` parameter is optional because Stripe enables its functionality by default.
            automatic_payment_methods={
                'enabled': True,
            },
        )
        #sauvegarde de l'intention de payement
        order.stripe_payment_intent = intent['client_secret']
        order.save()
        return JsonResponse({
            'clientSecret': intent['client_secret'],
        })
    except Exception as e:
        return JsonResponse({"error": str(e) })
    

def payment_success(request):
    return render (request, 'shop/payment_success.html' , {})
