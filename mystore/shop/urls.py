from django.urls import path
from shop.views import shop_view 

app_name="shop" #nom de l'app

urlpatterns = [
    path('', shop_view.index, name='home'),
    path('page/<str:slug>', shop_view.display_page, name='page'),
    path('product/<str:slug>', shop_view.display_product, name='single_product'),
    path('shop', shop_view.shop, name='shop_list'),

]
