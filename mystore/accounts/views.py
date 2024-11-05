from django.shortcuts import render
from accounts.forms.CustomUserRegisterForm import CustomUserRegisterForm

#Connexion
def signin(request):
    return render(request, 'accounts/signin.html', {})


#Inscription
def signup(request):
    form = CustomUserRegisterForm()
    return render(request, 'accounts/signup.html', {'form' : form})



def logout_user(request):
    pass

