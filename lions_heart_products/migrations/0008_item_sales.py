# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-10 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0007_auto_20171229_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sales',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='sales'),
        ),
    ]
