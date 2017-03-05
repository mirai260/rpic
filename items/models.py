from __future__ import unicode_literals
from django.db import models



class Item(models.Model):
    nom = models.CharField(max_length = 20)
    description = models.TextField(null = True, blank = True)

    def __str__(self):
        return self.nom


class Vendeur(models.Model):
    nom = models.CharField(max_length = 20)
    produits = models.ManyToManyField(Item, through="Offre")

    def __str__(self):
        return "Magasin de " + self.nom


class Offre(models.Model):
    vendeur = models.ForeignKey(Vendeur)
    item = models.ForeignKey(Item)
    prix = models.IntegerField()
    nombre = models.IntegerField(default = 10)

    def __str__(self):
        return self.vendeur.nom + " vend " + self.item.nom + " pour " + str(self.prix) + " pieces d'or."





