from django import forms
from accounts.models.Customer import Customer

class UserAccountForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'email')

        #Personnalisation des champs du formulaire via widget (attrs permet l'attribution d'attribut aux champs) : 
        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control custom-text-input'}),
        }