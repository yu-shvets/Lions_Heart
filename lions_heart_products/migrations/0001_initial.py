# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('title_uk', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='title')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='lions_heart_products.Category', verbose_name='parent сategory')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('title_uk', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='collection/logos', verbose_name='logo')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_uk', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'Сollection',
                'verbose_name_plural': 'Сollections',
            },
        ),
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('rate', models.FloatField()),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalog/products', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('title_uk', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_image', models.ImageField(upload_to='catalog/products', verbose_name='title image')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_uk', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='price')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('type', models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='Women', max_length=7, verbose_name='type')),
                ('sales', models.IntegerField(blank=True, null=True, verbose_name='sales')),
                ('unique_gift', models.BooleanField(default=False, verbose_name='unique gift')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_products.Category', verbose_name='сategory')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lions_heart_products.Collection', verbose_name='сollection')),
                ('recommended_items', models.ManyToManyField(blank=True, related_name='_item_recommended_items_+', to='lions_heart_products.Item', verbose_name='recommended')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Specs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='weight, gr')),
                ('diameter', models.FloatField(blank=True, null=True, verbose_name='diameter, mm')),
                ('length', models.FloatField(blank=True, null=True, verbose_name='length, mm')),
                ('specs', models.TextField(blank=True, null=True, verbose_name='other specs')),
                ('specs_uk', models.TextField(blank=True, null=True, verbose_name='other specs')),
                ('specs_ru', models.TextField(blank=True, null=True, verbose_name='other specs')),
                ('specs_en', models.TextField(blank=True, null=True, verbose_name='other specs')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_products.Item')),
            ],
            options={
                'verbose_name': 'Specs',
                'verbose_name_plural': 'Specs',
            },
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_products.Item', verbose_name='item'),
        ),
    ]
