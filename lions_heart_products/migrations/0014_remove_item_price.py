# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0013_auto_20180214_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
    ]
