from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dashboard.models.Address import Address
from dashboard.forms.AddressForm import AddressForm
from django.contrib import messages





@login_required
def address(request):
    user = request.user


    #On regarde si la requête est en post : 
    if request.method == "POST":
        address_form = AddressForm(request.POST)

        #Vérification de la validité du formulaire
        if address_form.is_valid():
            address = address_form.save(commit=False) #sauvegarde sans envois en base de donné
            address.author = user #Association de l'user à author
            address.save()
            messages.success(request, 'Adresse correctement ajoutée.')
            return redirect('dashboard:address')
            



    else:    
        address_form = AddressForm()
    
    addresses = Address.objects.filter(author=user)
    return render(request, 'dashboard/index.html', {'page': 'address', 'addresses' : addresses, 'address_form' : address_form})



@login_required
def edit_address(request, id):
    user = request.user
    address = get_object_or_404(Address, id=id, author=user)


    #On regarde si la requête est en post : 
    if request.method == "POST":
        #On vérife ensuite qu'on est bien en modification grace à _methode de l'input invisible : 
        if request.POST.get('_method') == 'PUT':
            address_form = AddressForm(request.POST, instance=address)

            #Vérification de la validité du formulaire 
            if address_form.is_valid():
                address.save()
                messages.success(request, 'Adresse correctement modifié.')
                return redirect('dashboard:address')
                
        else:
            messages.success(request, 'Erreur Serveur')
            return redirect('dashboard:address')
    else:    
        address_form = AddressForm(instance=address)
    
    
    return render(request, 'dashboard/index.html', {
        'page': 'address',
        'edit_address_form' : address_form
        })


@login_required
def delete_address(request,id):
    user = request.user
    address = get_object_or_404(Address, id=id, author=user)

    #On regarde si la requête est en post : 
    if request.method == "POST":
        #On vérife ensuite qu'on souhaite bien supprimer grace à _methode de l'input invisible : 
        if request.POST.get('_method') == 'DELETE':
            address.delete()
            messages.success(request, 'Adresse correctement supprimée.')
    
    return redirect('dashboard:address')
        

