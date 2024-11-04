from django.urls import path
from shop.views import shop_view , cart_view, compare_view

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



]
