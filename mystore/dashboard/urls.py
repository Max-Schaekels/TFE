from django.urls import path
from dashboard.views import dashboard_view
from dashboard.views import address_view
from dashboard.views import account_view



app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_view.index, name='home'),
    path('address', address_view.address, name='address'),
    path('address/<int:id>/edit', address_view.edit_address, name='edit_address'),
    path('address/<int:id>/delete', address_view.delete_address, name='delete_address'),

    # account
    path('account', account_view.index, name='account'),
    path('account/save', account_view.save_account, name='save_account'),   
    path('account/reset/password', account_view.reset_user_password, name='reset_user_password'),     
]
