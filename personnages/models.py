from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


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
	
	hp = models.IntegerField(null = True, blank = True)
	mana = models.IntegerField(null = True, blank = True)
	po = models.IntegerField(null = True, blank = True)
	
	traits = models.TextField(null = True, blank = True)
	competences = models.TextField(null = True, blank = True)
	sorts = models.TextField(null = True, blank = True)
	items = models.TextField(null = True, blank = True)
	descriptif = models.TextField(null = True, blank = True)
	
	def __str__(self):
		return self.nom


