from django.contrib import admin
from .models import Category, Product, Commande


# ce classe permet d'avoir un affichage convenable.
class AdminCategory(admin.ModelAdmin):
    list_display = ("name_cat", "date_added_cat")

class AdminProduct(admin.ModelAdmin):
    list_display = ("name_prod", "price_prod", "category", "date_added_prod")

class AdminCommande(admin.ModelAdmin):
    list_display = ("items","nom", "adresse", "email", "ville", "pays", "date_commande")

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)