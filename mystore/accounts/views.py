from django.shortcuts import render, redirect
from accounts.forms.CustomUserRegisterForm import CustomUserRegisterForm
from django.contrib import messages
from accounts.forms.CustomLoginForm import CustomLoginForm
from django.contrib.auth import authenticate, login, logout




#Connexion
def signin(request):
    #Vérification si l'utilisateur est déjà connecter
    if request.user.is_authenticated:
        return redirect('shop:home')

    #Vérification de la méthode
    if request.method == "POST":
        #Récupération du formulaire
        form = CustomLoginForm(data=request.POST)

        #Vérification de la validité du formulaire : 
        if form.is_valid():
            #récupération des informations 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            #vérification des informations récupérée ( si elles existent bien et sont correctes si pas bon on récupère None)
            user = authenticate(request, username=username, password=password)

            #Si user est correcte, on le connecte et on affiche un message
            if user is not None:
                login(request, user)
                messages.success(request, 'Vous êtes connnecté !')
                return redirect('dashboard:home')
            else:
                messages.error(request, 'Username ou Mot de passe incorrecte.')
        else:
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire')

    else:    
        #Création du formulaire d'authentification : 
        form = CustomLoginForm()
    return render(request, 'accounts/signin.html', {'form' : form})


#Inscription
def signup(request):
    #Vérification si l'utilisateur est déjà connecter
    if request.user.is_authenticated:
        return redirect('shop:home')
    #Vérification de la méthode
    if request.method == "POST":
        #récupération du formulaire : 
        form = CustomUserRegisterForm(request.POST)

        #Vérification de la validité du formulaire : 
        if form.is_valid() :
            #Sauvegarde du formulaire + message
            form.save()
            messages.success(request, 'Vous vous êtes bien inscrit ! ')
            return redirect('accounts:signin')
    else:
        #Création du formulaire :
        form = CustomUserRegisterForm()
    return render(request, 'accounts/signup.html', {'form' : form})



def logout_user(request):
    if request.user.is_authenticated:
        logout(request)


    return redirect('shop:home')    

