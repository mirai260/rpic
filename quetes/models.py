from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Quete(models.Model):
    titre = models.CharField(max_length = 50)
    description = models.TextField(null = True, blank = True)
    participants = models.ManyToManyField(User, blank = True)
    etatsPossible = (
        ("future", "Future quete"),
        ("enCours", "Quete en cours"),
        ("terminee", "Quete terminee")
    )
    etat = models.CharField(max_length = 20, choices = etatsPossible, default = "future")
    visible = models.BooleanField(default = False)

    def __str__(self):
        return self.titre

    class Meta:
	    permissions = (
	        ("voirQuetes", "voir les quetes cachees"),
        )





