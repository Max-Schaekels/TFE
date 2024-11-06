from typing import Any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from accounts.models.Customer import Customer


class CustomLoginForm(AuthenticationForm):

    #première méthode exécuté lorsqu'on rentre dans le formulaire
    def __init__(self, *args : Any, **kwargs : Any) -> None:
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field username
        self.fields['username'].widget.attrs["placeholder"] = 'Votre username' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field username
        self.fields['password'].widget.attrs["class"] = 'form-control' #Ajout d'un attribut class du widget du field password
        self.fields['password'].widget.attrs["placeholder"] = 'Mot de passe' #Ajout d'un attribut placeholder (texte par défaut tant que le champ est vide) au wigdet du field password


