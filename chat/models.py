from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    texte = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)



# Create your models here.
