from django import forms
from dashboard.models.Address import Address

class AddressForm(forms.ModelForm):
    #Les différents choix de type d'adresse avec le champ de formulaire auquel on attribue un attribut classe au widget 
    ADDRESS_TYPE_CHOICES = [('billing', 'Billing'), ('shipping', 'Shipping')] #Précision s'il s'agit de l'adresse de livraison ou de facturation 

    address_type = forms.ChoiceField(
        choices=ADDRESS_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control custom-text-input'})
    )

    class Meta:
        model = Address
        fields = ('name', 'full_name', 'street', 'code_postal', 'city', 'country', 'more_details', 'address_type')

        #Personnalisation des champs du formulaire via widget (attrs permet l'attribution d'attribut aux champs) : 
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'full_name' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'street' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'code_postal' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'city' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'country' : forms.TextInput(attrs={'class': 'form-control custom-text-input'}),
            'more_details' : forms.Textarea(attrs={'class': 'form-control custom-textarea'}),

        }
