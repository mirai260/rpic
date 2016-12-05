# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-04 13:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FichePerso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('hp', models.IntegerField(blank=True, null=True)),
                ('mana', models.IntegerField(blank=True, null=True)),
                ('PO', models.IntegerField(blank=True, null=True)),
                ('traits', models.TextField(blank=True, null=True)),
                ('competences', models.TextField(blank=True, null=True)),
                ('sorts', models.TextField(blank=True, null=True)),
                ('items', models.TextField(blank=True, null=True)),
                ('descriptif', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ficheperso',
            name='perso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personnages.Perso'),
        ),
    ]