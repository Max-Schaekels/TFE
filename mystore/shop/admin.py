from django.contrib import admin
from shop.models.Slider import Slider
from shop.models.Collection import Collection
from shop.models.Product import Product
from shop.models.Category import Category
from django.utils.html import format_html
from shop.models.Image import Image

#Gestion des donnée affichée sur la page concernant les Sliders : 
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','display_image') #ce qui est afficher sur le pannel admin
    list_display_links = ('title',) #ce sur quoi on peut cliquer

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150" />')
    
    display_image.short_description = 'image'

#Gestion des donnée affichée sur la page concernant les Collections : 
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','display_image') #ce qui est afficher sur le pannel admin
    list_display_links = ('title',) #ce sur quoi on peut cliquer

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150" />')
    
    display_image.short_description = 'image'

#Gestion des donnée affichée sur la page concernant les catégories : 
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','display_image') #ce qui est afficher sur le pannel admin
    list_display_links = ('name',) #ce sur quoi on peut cliquer

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150" />')
    
    display_image.short_description = 'image'
    exclude = ('slug',) #exclus le champ slug du pannel admin

#Classe pour permettre l'ajout d'image lors de la création d'un produit via panel admin
class ImageInline(admin.TabularInline):
    model = Image
    extra = 3

#Gestion des donnée affichée sur la page concernant les catégories : 
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ('id', 'name', 'solde_price', 'regular_price','is_best_seller', 'is_new_arrival', 'is_featured', 'is_special_offer', 'display_image') #ce qui est afficher sur le pannel admin
    list_display_links = ('name',) #ce sur quoi on peut cliquer
    list_editable =('is_best_seller', 'is_new_arrival', 'is_featured', 'is_special_offer') #permet d'éditer ces paramètres dans le panneau admin sans passer par la page du produit
    list_per_page = 5

    def display_image(self, obj):
        first_image = obj.images.first()
        if not first_image: #dans le cas ou il n'y a pas d'image
            return ''
        return format_html(f'<img src="{first_image.image.url}" heigth="90" width="80" />')
    
    exclude = ('slug',) #exclus le champ slug du pannel admin
    
    display_image.short_description = 'image'


#Autorisation de gérer les slides via la page admin du site : 
admin.site.register(Slider, SliderAdmin)
#Autorisation de gérer les collections via la page admin du site : 
admin.site.register(Collection, CollectionAdmin)
#Autorisation de gérer les catégories via la page admin du site : 
admin.site.register(Category, CategoryAdmin)
#Autorisation de gérer les produits via la page admin du site : 
admin.site.register(Product, ProductAdmin)
