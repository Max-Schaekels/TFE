from django.db import models
from django.utils.text import slugify

class Carrier(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120,blank=False, null=False)
    details = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to="carrier_images", blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta : #gestion du nom afficher dans le pannel admin du site 
        verbose_name = 'Transporteur'
        verbose_name_plural = 'Transporteurs'


    def __str__(self): #affichage sous forme de chaine de caractère
        return f"{self.name} ( {self.price} €)"