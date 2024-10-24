from django.contrib import admin
from shop.models.Slider import Slider
from django.utils.html import format_html

#Gestion des donnée affichée sur la page concernant les Sliders : 
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','display_image')

    def display_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="150" />')
    
    display_image.short_description = 'image'




#Autorisation de gérer les slides via la page admin du site : 
admin.site.register(Slider, SliderAdmin)
