# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-13 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20161213_0910'),
    ]

    operations = [
        migrations.AddField(
            model_name='offre',
            name='nombre',
            field=models.IntegerField(default=10),
        ),
    ]
