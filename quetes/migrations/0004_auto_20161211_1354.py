# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-11 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quetes', '0003_quete_visible'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quete',
            options={'permissions': (('voirQuetes', 'voir les quetes cachees'),)},
        ),
    ]
