# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-22 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_blog', '0010_auto_20180222_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='review',
            field=models.TextField(max_length=1332, verbose_name='review'),
        ),
    ]
