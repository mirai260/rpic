# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-11 11:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quetes', '0002_auto_20161211_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='quete',
            name='visible',
            field=models.BooleanField(default=False),
        ),
    ]
