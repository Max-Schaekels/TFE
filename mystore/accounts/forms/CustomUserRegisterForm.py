from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models.Customer import Customer


class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    #première méthode exécuté lorsqu'on rentre dans le formulaire
    def __init__(self, *args : Any, **kwargs : Any) -> None:
        super(CustomUserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field username
        self.fields['username'].widget.attrs["placeholder"] = 'Username' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field username
        self.fields['email'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field email
        self.fields['email'].widget.attrs["placeholder"] = 'Email' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field email
        self.fields['password1'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field password1
        self.fields['password1'].widget.attrs["placeholder"] = 'Mot de passe' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field password1
        self.fields['password2'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field password2
        self.fields['password2'].widget.attrs["placeholder"] = 'Confirmer votre mot de passe' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field password2
        self.fields['agree_terms'].widget.attrs["class"] = 'form-check-input' #Ajout d'un attribut classe au wigdet du field agree_terms

    class Meta:
        #model utilisé pour le formulaire :
        model = Customer 
        #champ utilisé dans le formulaire :
        fields = ('username', 'email','agree_terms', 'password1', 'password2' )

