# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-28 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_auto_20190128_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', unique=False),
            preserve_default=False,
        ),
    ]
