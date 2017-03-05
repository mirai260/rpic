from __future__ import unicode_literals

from django.db import models

class Background(models.Model):
    titre = models.CharField(max_length = 30)
    sujets = (("edelia","Histoire d'Edelia"),("isep","Background des membres de l'Isep"))
    sujet = models.CharField(max_length = 10, choices = sujets, default = "edelia")
    histoire = models.TextField(null = True, blank = True)

    def __str__(self):
	    return self.titre