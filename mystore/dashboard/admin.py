from django.contrib import admin
from dashboard.models.Address import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'full_name', 'street', 'code_postal', 'city', 'country', 'address_type', 'author')
    list_filter = ('address_type', 'author', 'created_at', 'updated_at')
    search_fields = ('name', 'full_name', 'street', 'code_postal', 'city', 'country', 'address_type', 'author__username')

admin.site.register(Address)