# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-16 10:08
from __future__ import unicode_literals

from django.db import migrations
import positions.fields


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0016_item_best_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='position',
            field=positions.fields.PositionField(default=-1),
        ),
    ]
