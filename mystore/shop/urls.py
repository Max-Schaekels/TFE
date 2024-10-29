from django.urls import path
from shop.views.shop_view import index, display_page

urlpatterns = [
    path('', index, name='home'),
    path('page/<str:slug>', display_page, name='page'),
]
