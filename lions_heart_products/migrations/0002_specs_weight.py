# Generated by Django 2.0 on 2017-12-17 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lions_heart_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='specs',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='вес'),
        ),
    ]