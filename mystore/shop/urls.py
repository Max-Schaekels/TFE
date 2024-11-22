from django.urls import path
from shop.views import shop_view , cart_view, compare_view, wishlist_view, checkout_view

app_name="shop" #nom de l'app

urlpatterns = [
    #Shop
    path('', shop_view.index, name='home'),
    path('page/<str:slug>', shop_view.display_page, name='page'),
    path('product/<str:slug>', shop_view.display_product, name='single_product'),
    path('shop', shop_view.shop, name='shop_list'),

    #Cart (panier)
    path('cart', cart_view.index, name='cart'),
    path('cart/add/<int:product_id>', cart_view.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/<int:quantity>', cart_view.remove_from_cart, name='remove_from_cart'),

    #Comparaison
    path('compare', compare_view.index, name='compare'),
    path('compare/add/<int:product_id>', compare_view.add_to_compare, name='add_to_compare'),
    path('compare/remove/<int:product_id>', compare_view.remove_from_compare, name='remove_from_compare'),

    #Liste des souhaits
    path('wishlist', wishlist_view.index, name='wishlist'),
    path('wishlist/add/<int:product_id>', wishlist_view.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:product_id>', wishlist_view.remove_from_wishlist, name='remove_from_wishlist'),

    #Checkout
    path('checkout', checkout_view.index, name='checkout'),
    path('checkout/add_address', checkout_view.add_address, name='add_address'),

]
