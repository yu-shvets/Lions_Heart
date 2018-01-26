# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-26 10:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(blank=True, max_length=256, null=True, verbose_name='author')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='CompanyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='company/pictures', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Diploma',
                'verbose_name_plural': 'Diplomas',
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(verbose_name='about')),
                ('about_uk', models.TextField(null=True, verbose_name='about')),
                ('about_ru', models.TextField(null=True, verbose_name='about')),
                ('about_en', models.TextField(null=True, verbose_name='about')),
                ('about_title_image', models.ImageField(blank=True, null=True, upload_to='company/pictures', verbose_name='about_image')),
                ('center_banner', models.ImageField(blank=True, null=True, upload_to='company/pictures', verbose_name='center_banner')),
                ('left_banner', models.ImageField(blank=True, null=True, upload_to='company/pictures', verbose_name='left_banner')),
                ('right_banner', models.ImageField(blank=True, null=True, upload_to='company/pictures', verbose_name='right_banner')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.CompanyInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/pictures', verbose_name='image')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=256)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.CompanyInformation')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='name')),
                ('title_uk', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_ru', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='name')),
                ('body_text', models.TextField(blank=True, null=True, verbose_name='text')),
                ('body_text_uk', models.TextField(blank=True, null=True, verbose_name='text')),
                ('body_text_ru', models.TextField(blank=True, null=True, verbose_name='text')),
                ('body_text_en', models.TextField(blank=True, null=True, verbose_name='text')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='blog/pictures', verbose_name='main image')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'abstract': False,
                'ordering': ['-created'],
            },
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.Post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='companyimage',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.CompanyInformation'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.Post', verbose_name='post'),
        ),
        migrations.AddField(
            model_name='address',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.CompanyInformation'),
        ),
    ]
