# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-10 17:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnages', '0007_auto_20161207_0830'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ficheperso',
            options={'permissions': (('voirFichePerso', 'voir fiche perso'),)},
        ),
    ]
