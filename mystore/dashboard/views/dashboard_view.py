from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models.Address import Address


@login_required
def index(request):
    return render(request, 'dashboard/index.html', {'page': 'index'})


@login_required
def address(request):
    user = request.user
    addresses = Address.objects.filter(author=user)
    return render(request, 'dashboard/index.html', {'page': 'address', 'addresses' : addresses})