from django.db import models

# Create your models here.
class Category(models.Model):

    name_cat = models.CharField(max_length=100)
    date_added_cat = models.DateTimeField(auto_now=True)

# la class Meta nous permet d'ordonner les catégories à chaque enrégistrement
    class Meta:
# on met un signe - devant la table pour l'avoir toujours à la premiere ligne    
        ordering = ["-date_added_cat"]

    def __str__(self):
        return self.name_cat


class Product(models.Model):
    
    name_prod = models.CharField(max_length=150)
    price_prod = models.FloatField()
    description_prod = models.TextField()
# Etablir la relation entre les produits et la catégorie
    category = models.ForeignKey(Category, related_name="cat_prod_id", on_delete=models.CASCADE)
    image_prod = models.CharField(max_length=500)
    date_added_prod = models.DateTimeField(auto_now=True)
    class Meta:
# on met un signe - devant la table pour l'avoir toujours à la premiere ligne    
        ordering = ["-date_added_prod"]

    def __str__(self):
        return self.name_prod