from django.shortcuts import render
from shop.models.Slider import Slider
from shop.models.Collection import Collection
from shop.models.Product import Product


def index(request):
    sliders = Slider.objects.all()
    collections = Collection.objects.all()

    best_sellers = Product.objects.filter(is_best_seller=True)
    new_arrivals = Product.objects.filter(is_new_arrival=True)
    featured = Product.objects.filter(is_featured=True)
    special_offers = Product.objects.filter(is_special_offer=True)
    

    return render(request, 'shop/index.html', {
        'sliders' : sliders,
        'collections' : collections,
        'new_arrivals' : new_arrivals,
        'best_sellers' : best_sellers,
        'featured' : featured,
        'special_offers' : special_offers,

        })