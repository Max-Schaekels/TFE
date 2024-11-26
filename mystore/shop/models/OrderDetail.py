from django.db import models
from shop.models.Order import Order

#Les informations sont stocker "en dur" et pas mis en relation
#afin d'éviter si jamais il y a un changement dans le futur notament dans le prix
#les anciennes commandes ne soient pas impactées. 

class OrderDetail(models.Model):
    product_name = models.CharField(max_length=255)
    product_description = models.TextField()
    solde_price = models.IntegerField()
    regular_price = models.IntegerField()
    quantity = models.IntegerField()
    taxe = models.IntegerField()
    sub_total_ht = models.IntegerField()
    sub_total_ttc = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Relation avec le modèle Order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Détail de la commande {self.id} - {self.product_name}"