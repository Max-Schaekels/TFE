from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name='format_price') #décorateur qui enregistre la fonction
@stringfilter #decorateur expliquant que la fonction ci-dessous est un filtre
def format_price(value):
    try :
        value = float(value)

        return '{:.2f} €'.format(value) #formatage de la valeur pour afficher 2 chiffres après virugle après transformation en nmbr flottant
    except:
        return value
    

@register.filter(name='solde_rate') 
def solde_rate(product):
    try :
        solde_price = float(product.solde_price)
        regular_price = float(product.regular_price)

        rate = ((regular_price - solde_price)/ regular_price)*100

        return f"- {int(rate)} %"
    except:
        return f"{0} %" 