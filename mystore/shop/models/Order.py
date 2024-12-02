from django.db import models
from accounts.models.Customer import Customer


#Les informations sur le transporteur sont stocker en dur et pas mis en relation
#afin d'éviter si jamais il y a un changement dans le futur notament dans le prix
#les anciennes commandes ne soient pas impactées. 

#author est une foreign key mais on le protège de la supression au cas ou l'utilisateur supprimer son compte, on veut pouvoir concerver la commande. 


class Order(models.Model):
    client_name = models.CharField(max_length=255)
    billing_address = models.CharField(max_length=255)
    shipping_address = models.CharField(max_length=255)
    quantity = models.IntegerField()
    taxe = models.FloatField()
    author = models.ForeignKey(Customer, on_delete=models.PROTECT)
    order_cost = models.FloatField()
    order_cost_ttc = models.FloatField()
    is_paid = models.BooleanField(default=False)
    carrier_name = models.CharField(max_length=255)
    carrier_price = models.FloatField()
    payment_method = models.CharField(max_length=255)
    stripe_payment_intent = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Commande {self.id} - {self.client_name}"
