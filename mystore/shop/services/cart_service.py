
from django.contrib import messages
from shop.models import Carrier, Setting, Product  

class CartService:
    @staticmethod  #permet de ne pas instancier la classe pour utiliser les méthodes
    def add_to_cart(request, product_id, quantity):
        cart = request.session.get('cart', {}) #recuperation du panier de la session
        product_id = str(product_id)
        
        if product_id in cart:
            cart[product_id] += quantity
        else:
            cart[product_id] = quantity
        
        request.session['cart'] = cart
        messages.success(request, f"Produit ajouté au panier.")
    
    @staticmethod
    def remove_from_cart(request, product_id, quantity):
        cart = request.session.get('cart', {}) #recuperation du panier de la session
        product_id = str(product_id)
        
        if product_id in cart:
            if cart[product_id] <= quantity:
                del cart[product_id]
            else:
                cart[product_id] -= quantity
        
        request.session['cart'] = cart
        messages.success(request, f"Produit supprimé du panier.")
    
    @staticmethod
    def clear_cart(request):
        request.session.pop('cart', None)
        messages.success(request, f"Le panier a été vidé.")
    
    @staticmethod
    def get_cart_details(request): #récupère les détails du panier
        cart = request.session.get('cart', {}) #recuperation du panier de la session
        setting = Setting.objects.first() #récupération des paramètres
        tax_rate = setting.taxe_rate / 100 if setting else 0 
        
        result = {
            'items': [],
            'sub_total': 0,
            'carrier_name': 0,
            'shipping_price': 0,
            'taxe_amount': 0,
            'sub_total_ht': 0,
            'sub_total_ttc': 0,
            'sub_total_with_shipping': 0,
            'cart_count': 0,
        }
        carrier_data = request.session.get('carrier') #recupération du transporteur
        if not carrier_data:
            carrier = Carrier.objects.first()
        else:
            carrier = Carrier(**carrier_data)


        for product_id, quantity in cart.items():
            product = Product.objects.filter(id=product_id).first() #récupération du produit en filtrant par l'id
            
            if product:
                sub_total = product.solde_price * quantity
                result['items'].append({
                    'product': {
                        'id': product.id,
                        'slug': product.slug,
                        'name': product.name,
                        'description': product.description,
                        'image' : product.images.first().image.url,
                        'solde_price': product.solde_price,
                        'regular_price': product.regular_price,
                        
                    },
                    'quantity': quantity,
                    'sub_total': round(sub_total, 2),
                    'taxe_amount': round(sub_total / (1 + tax_rate) * tax_rate, 2),
                    'sub_total_ht': round(sub_total / (1 + tax_rate), 2),
                    'sub_total_ttc': round(sub_total, 2),
                })
                result['sub_total'] += round(sub_total, 2)
                result['cart_count'] += quantity
        
        result['carrier_id'] = carrier.id
        result['carrier_name'] = carrier.name
        result['shipping_price'] = round(carrier.price, 2)
        result['taxe_amount'] = round(result['sub_total'] / (1 + tax_rate) * tax_rate, 2)
        result['sub_total_ht'] = round(result['sub_total'] / (1 + tax_rate), 2)
        result['sub_total_ttc'] = round(result['sub_total'], 2)
        result['sub_total_with_shipping'] = round(result['sub_total'] + carrier.price, 2)
        
        return result


    