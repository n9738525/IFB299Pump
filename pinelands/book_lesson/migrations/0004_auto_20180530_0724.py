# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lesson', '0003_instruments_instrument_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruments',
            name='instrument_name',
            field=models.CharField(max_length=128),
        ),
    ]
