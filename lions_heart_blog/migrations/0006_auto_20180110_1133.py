# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-10 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_blog', '0005_auto_20171229_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinformation',
            name='title_image_1',
            field=models.ImageField(null=True, upload_to='company/pictures', verbose_name='title_image_1'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='title_image_2',
            field=models.ImageField(null=True, upload_to='company/pictures', verbose_name='title_image_2'),
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='title_image_3',
            field=models.ImageField(null=True, upload_to='company/pictures', verbose_name='title_image_3'),
        ),
    ]