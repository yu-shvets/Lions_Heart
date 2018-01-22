# Generated by Django 2.0 on 2017-12-17 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('author', models.CharField(blank=True, max_length=256, null=True, verbose_name='автор')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created'],
                'verbose_name': 'Комментарий',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog/pictures', verbose_name='изображение')),
            ],
            options={
                'verbose_name_plural': 'изображения',
                'verbose_name': 'Изображение',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, verbose_name='наименование')),
                ('body_text', models.TextField(blank=True, null=True, verbose_name='содержание')),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='blog/pictures', verbose_name='титульное изображение')),
            ],
            options={
                'verbose_name_plural': 'Посты',
                'ordering': ['-created'],
                'verbose_name': 'Пост',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='image',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.Post', verbose_name='пост'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lions_heart_blog.Post', verbose_name='пост'),
        ),
    ]