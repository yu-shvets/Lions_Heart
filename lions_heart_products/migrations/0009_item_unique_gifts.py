# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-14 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0008_item_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='unique_gifts',
            field=models.BooleanField(default=False, verbose_name='unique gifts'),
        ),
    ]