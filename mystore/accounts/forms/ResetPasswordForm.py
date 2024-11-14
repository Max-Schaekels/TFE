from django import forms
from django.contrib.auth import authenticate


class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))

    class Meta:
        fields = ('old_password', 'new_password1', 'new_password2')

    #Méthode pour vérifier les mots de passes lors de la modification
    def clean(self):
        cleaned_data = super().clean() #récupération des informations hérité nettoyée
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        user = self.user 

        #On vérifie si on peut connecter l'utilisateur avec old_password
        user_authenticated = authenticate (username=user.username, password=old_password)

        #Si on peu pas le connecter, message d'erreur
        if not user_authenticated:
            self.add_error('old_password', 'Mauvais ancien mot de passe. Veuillez réessayer.')

        #On vérifie si les nouveaux mdp sont les mêmes
        if new_password1 != new_password2:
            self.add_error('new_password2', 'Les nouveaux mot de passes ne correspondent pas')

        return cleaned_data