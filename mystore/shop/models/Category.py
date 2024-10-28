from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=60, blank=False, null=False)
    description = models.CharField(max_length=120,blank=False, null=False)
    slug = models.SlugField(max_length=255,blank=False, null=False)
    image = models.ImageField(upload_to="category_images", blank=False, null=False)
    is_mega = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta : #gestion du nom afficher dans le pannel admin du site (soit category ou categories)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs) : #création du champ slug lors de la création dans le panel admin
        if not self.slug :
            self.slug = slugify(self.name)
        super().save( *args, **kwargs)

    def __str__(self): #affichage sous forme de chaine de caractère
        return self.name