from django.contrib import admin
from .models import Category, Product, Commande


# ce classe permet d'avoir un affichage convenable.

# Changer le nom de l'interface
admin.site.site_header = "Diole_Familiy_Shop"
admin.site.site_title = "DF_Shop" # nommer la page du site
admin.site.index_title = "Manageur"
class AdminCategory(admin.ModelAdmin):
    list_display = ("name_cat", "date_added_cat")

class AdminProduct(admin.ModelAdmin):
    list_display = ("name_prod", "price_prod", "category", "date_added_prod")
    search_fields = ("name_prod",)
    list_editable = ("price_prod",)

class AdminCommande(admin.ModelAdmin):
    list_display = ("items", "prix", "nom", "adresse", "email", "ville", "pays", "date_commande")

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)