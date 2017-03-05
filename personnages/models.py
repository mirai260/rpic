from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from items.models import Item


def renommage(perso, name):
	nomFichier = "imagesPerso/"+perso.nom+".jpg"
	return nomFichier


class Perso(models.Model):
	nom = models.CharField(max_length=20)
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to=renommage, null = True, blank = True)

	def __str__(self):
		return self.nom



class FichePerso(models.Model):
	nom = models.CharField(max_length = 20)
	perso = models.ForeignKey(Perso)
	lvl = models.IntegerField(null = True, blank = True)
	hp = models.IntegerField(null = True, blank = True)
	mana = models.IntegerField(null = True, blank = True)
	po = models.IntegerField(null = True, blank = True)

	traits = models.TextField(null = True, blank = True)
	competences = models.TextField(null = True, blank = True)
	sorts = models.TextField(null = True, blank = True)
	items = models.TextField(null = True, blank = True)
	item = models.ManyToManyField(Item, through = 'Possession')
	descriptif = models.TextField(null = True, blank = True)
	etatsPossible = (("EnVie", "En vie"),("Mort", "Mort"),("Disparu", "Disparu"))
	etat = models.CharField(max_length = 20, choices = etatsPossible, default = "EnVie")

	extra = models.URLField(null = True, blank = True)

	def __str__(self):
		return self.nom

	class Meta:
	    permissions = (
	        ("voirFichePerso", "voir fiche perso"),
        )


class Possession(models.Model):
    nombre = models.IntegerField()
    item = models.ForeignKey(Item)
    fichePerso = models.ForeignKey(FichePerso)

    def __str__(self):
        return self.fichePerso.perso.nom + " possede " + str(self.nombre) + " " + self.item.nom

