# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_type',
            field=models.CharField(choices=[('Карта', 'Карта'), ('Наличные', 'Наличные')], default='Карта', max_length=11, verbose_name='способ платежа'),
        ),
    ]