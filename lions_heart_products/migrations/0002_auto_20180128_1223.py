# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-28 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specs',
            name='height',
            field=models.FloatField(blank=True, null=True, verbose_name='height, mm'),
        ),
        migrations.AddField(
            model_name='specs',
            name='width',
            field=models.FloatField(blank=True, null=True, verbose_name='width, mm'),
        ),
    ]