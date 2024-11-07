from django.urls import path
from dashboard.views import dashboard_view


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard_view.index, name='home'),
    path('address', dashboard_view.address, name='address'),
    path('address/<int:id>/edit', dashboard_view.edit_address, name='edit_address'),
    path('address/<int:id>/delete', dashboard_view.delete_address, name='delete_address'),
]
