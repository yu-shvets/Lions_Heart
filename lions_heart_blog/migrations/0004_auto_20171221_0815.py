# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-21 08:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_blog', '0003_auto_20171219_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinformation',
            name='about_en',
            field=models.TextField(null=True, verbose_name='информация о компании'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='about_ru',
            field=models.TextField(null=True, verbose_name='информация о компании'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='address_en',
            field=models.CharField(max_length=256, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='address_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='post',
            name='body_text_en',
            field=models.TextField(blank=True, null=True, verbose_name='содержание'),
        ),
        migrations.AddField(
            model_name='post',
            name='body_text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='содержание'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en',
            field=models.CharField(max_length=256, null=True, verbose_name='наименование'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=256, null=True, verbose_name='наименование'),
        ),
    ]
