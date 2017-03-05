# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-11 11:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quetes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quete',
            name='fini',
        ),
        migrations.AddField(
            model_name='quete',
            name='etat',
            field=models.CharField(choices=[('future', 'Future quete'), ('enCours', 'Quete en cours'), ('terminee', 'Quete terminee')], default='future', max_length=20),
        ),
    ]
