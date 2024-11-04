from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from shop.models.Slider import Slider
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Page import Page
from shop.models.Category import Category


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


    #Récupération de toutes les catégories :
    categories = Category.objects.all()

    # Récupéaration du paramètre de tri par prix depuis la session, valeur par défaut : asc
    sort_by_price = request.session.get('sort-price', 'asc')

    # Récupération du nombre d'éléments à afficher par page depuis la session, valeur par défaut : 6  
    showing = int(request.session.get('showing', 6)) 

    # Récupération de la catégorie, valeur par défaut : all
    category_id = request.GET.get('category_id', 'all')

    if category_id and category_id != 'all':
        category = get_object_or_404(Category, id=category_id) #récupération de la catégorie ou renvois page 404
        products = category.product_set.all()  #récupération des produits de la catégorie
    else :
        products = Product.objects.all()  #Récupération de tous les produits 



    # Mise à jour du nombre d'éléments à afficher par page si présent dans les paramètres de requête
    if 'showing' in request.GET and request.GET['showing'] != "" :
        showing = request.GET['showing']
        request.session['showing'] = showing

 
    if 'category_id' in request.GET and request.GET['category_id'] != "" :
        category_id = request.GET['category_id']


    # Mise à jour du paramètre de tri par prix si présent dans les paramètres de requête    
    if 'sort-price' in request.GET and request.GET['sort-price'] != "" :
        sort_by_price = request.GET['sort-price']
        request.session['sort-price'] = sort_by_price
   

    page = request.GET.get('page', 1) #récupération de la page via url, si rien préciser dans url page par défaut : page 1
    display = request.session.get('display', 'grid') #récupération du type de display lors de la session valeur par défaut : grid

    # Mise à jour du paramètre d'affichage si présent dans les paramètres de requête  
    if 'display' in request.GET : 
        display = request.GET['display']
        request.session['display'] = display 


    # Tri des produits en fonction du paramètre sort_by_price
    if sort_by_price == "asc" :
        products = products.order_by('solde_price')
    elif sort_by_price == "desc" :
        products = products.order_by('-solde_price')

    paginator = Paginator(products, showing) #pagination du nombre de produit par page, valeur par défaut = showing

    try :
        products_page = paginator.page(page)

    except PageNotAnInteger: #gestion des cas de chaine de caractère ne correspondant pas à la demande rentrer en url 
        products_page = paginator.page(1)

    except EmptyPage: #gestion des cas ou le nombre mis en url est supérieur au nombre de page
        products_page = paginator.page(paginator.num_pages)

    except:
        products_page = paginator.page(1)

   #envois des infos au template pour premettre leur utilisation :
    return render(request, 'shop/shop_list.html', {
        'products' : products_page,
        'categories' : categories,
        'display' : display,
        'sort_by_price' : sort_by_price,
        'default_category_id' : int(category_id) if category_id.isdigit() else category_id,

        })
