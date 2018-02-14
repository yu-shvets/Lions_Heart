# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-14 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_blog', '0004_banners_is_revived'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyinformation',
            name='center_banner',
        ),
        migrations.RemoveField(
            model_name='companyinformation',
            name='left_banner',
        ),
        migrations.RemoveField(
            model_name='companyinformation',
            name='right_banner',
        ),
        migrations.AddField(
            model_name='companyinformation',
            name='banner_title',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]