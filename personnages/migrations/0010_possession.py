# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-12 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20161212_1702'),
        ('personnages', '0009_ficheperso_extra'),
    ]

    operations = [
        migrations.CreateModel(
            name='Possession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.IntegerField()),
                ('fichePerso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnages.FichePerso')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Item')),
            ],
        ),
    ]