from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms.UserAccountForm import UserAccountForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from accounts.forms.ResetPasswordForm import ResetPasswordForm



def index(request) :
    user = request.user
    account_form = UserAccountForm(instance=user)
    reset_password_form = ResetPasswordForm()
    reset_password_form.user = user    

    return render(request, 'dashboard/index.html', {
        'page' : 'account',
        'account_form' : account_form,
        'reset_password_form' : reset_password_form,
        })

def save_account(request) :
    user = request.user
    #Vérification de la méthode pour savoir si on consulte ou modifie les données : 
    if request.method == "POST":
        account_form = UserAccountForm(request.POST, instance=user)
        #Vérification si le formulaire est valide :
        if account_form.is_valid():
            #sauvegarde des données 
            account_form.save()
            messages.success(request, 'Modifications enregistrées.')
            return redirect('dashboard:account')
        else :
            #message d'erreur 
            messages.success(request, 'Erreur détectées.')
            return redirect('dashboard:account')


    return redirect('dashboard:account')

def reset_user_password(request):
    user = request.user 
    if request.method == "POST":
        reset_password_form = ResetPasswordForm(request.POST)
        reset_password_form.user = user
        if reset_password_form.is_valid():
            # sauvegarde du nouveau password
            new_password = reset_password_form.cleaned_data['new_password1']
            #Mise à jour du mot de passe de l'utilisateur
            user.set_password(new_password) 
            #Sauvegarde de l'utilisateur modifier dans la base de donnée
            user.save()
            
            #Mise à jour de la session
            update_session_auth_hash(request, user)
            messages.success(request, 'Mot de passe changer avec succès.')
            return redirect('dashboard:account')
        else:
            account_form = UserAccountForm(instance=user)
            messages.success(request, 'Erreur dans le changement de mot de passse. Vérifier le formulaire.')
            return render(request, 'dashboard/index.html', {
                'page': 'account',
                'account_form': account_form,
                'reset_password_form': reset_password_form,
                })
        
    return redirect('dashboard:account')