from django.db import models
from django.contrib.auth.models import User
from personnages.models import Perso

class Profil(models.Model):
    user = models.OneToOneField(User)
    personnagePrincipal = models.OneToOneField(Perso, null=True, blank=True)
    prenom = models.CharField(max_length = 20, null=True, blank=True)
    nom = models.CharField(max_length = 20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "Profil de {0}".format(self.user.username)


