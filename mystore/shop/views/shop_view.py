from django.shortcuts import render
from shop.models.Slider import Slider
from shop.models.Collection import Collection

def index(request):
    sliders = Slider.objects.all()
    collections = Collection.objects.all()
    return render(request, 'shop/index.html', {
        'sliders' : sliders,
        'collections' : collections
        })