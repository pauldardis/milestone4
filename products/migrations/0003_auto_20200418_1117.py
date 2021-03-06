# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-18 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200412_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brief_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='full_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default='', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
