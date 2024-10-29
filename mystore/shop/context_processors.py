from shop.models.Setting import Setting
from shop.models.Social import Social
from shop.models.Page import Page



#Page ayant pour but de permettre de transmettre plus facilement les informations des models Setting et Social à tous les templates actuelles et futurs du site

def site_settings(request):
    site_settings = Setting.objects.first()
    socials = Social.objects.all()
    head_pages = Page.objects.filter(is_head=True)
    foot_pages = Page.objects.filter(is_foot=True)
    my_socials = []
    my_head_pages = []
    my_foot_pages = []

    for item in socials : #On place les données de socials qui sont récupérer en querry dans une liste afin que la session puisse correctement les comprendres
        my_socials.append({
            'name' : item.name,
            'icon' : item.icon,
            'link' : item.link,
        })

    for item in head_pages : #Pareil que pour Social mais pour head page
        my_head_pages.append({
            'name' : item.name,
            'slug' : item.slug
        })

    for item in foot_pages : #Pareil que pour head mais pour foot page
        my_foot_pages.append({
            'name' : item.name,
            'slug' : item.slug
        })

    context = {
        'name' : site_settings.name,
        'description' : site_settings.description,
        'email' : site_settings.email,
        'phone' : site_settings.phone,
        'currency' : site_settings.currency,
        'street' : site_settings.street,
        'city' : site_settings.city,
        'code_postal' : site_settings.code_postal,
        'state' : site_settings.state,
        'copyright' : site_settings.copyright,
        'socials' : my_socials,
        'head_pages' : my_head_pages,
        'foot_pages' : my_foot_pages,

    }

    request.session.update(context)

    return context