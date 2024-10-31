from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from shop.models.Slider import Slider
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Page import Page


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

def display_page(request, slug):
    page = get_object_or_404(Page, slug=slug)

    return render(request, 'shop/page.html', {
        'page' : page,
        })


def display_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
   
    return render(request, 'shop/single_product.html', {
        'product' : product,
        })

def shop(request):

    products = Product.objects.all()

    sort_by_price = request.session.get('sort-price', 'asc')
    if 'sort-price' in request.GET and request.GET['sort-price'] != "" :
        sort_by_price = request.GET['sort-price']
        request.session['sort-price'] = sort_by_price


    showing = request.session.get('showing', 6) #récupération du showing et mise par défaut de la valeur 
    #vérification du showing : 
    if 'showing' in request.GET and request.GET['showing'] != "" :
        showing = request.GET['showing']
        request.session['showing'] = showing


   

    page = request.GET.get('page', 1) #récupération de la page via url, si rien préciser dans url page par défaut = page 1
    display = request.session.get('display', 'grid') #récupération du type de display lors de la session 

    if 'display' in request.GET : #vérification du display et update de la session. 
        display = request.GET['display']
        request.session['display'] = display 

    if sort_by_price == "asc" :
        products = products.order_by('solde_price')
    elif sort_by_price == "desc" :
        products = products.order_by('-solde_price')

    paginator = Paginator(products, showing) #pagination du nombre de produit par page, valeur par défaut = showing

    try :
        products_page = paginator.page(page)

    except PageNotAnInteger: #gestion des cas de chaine de caractère rentrer en url
        products_page = paginator.page(1)

    except EmptyPage: #gestion des cas ou le nombre mis en url est supérieur au nombre de page
        products_page = paginator.page(paginator.num_pages)

    except:
        products_page = paginator.page(1)
   
    return render(request, 'shop/shop_list.html', {
        'products' : products_page,
        'display' : display,
        'sort_by_price' : sort_by_price,
        })
