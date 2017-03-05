# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 17:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20161212_1702'),
        ('personnages', '0010_possession'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficheperso',
            name='item',
            field=models.ManyToManyField(through='personnages.Possession', to='items.Item'),
        ),
    ]
