# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-30 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lesson', '0005_auto_20180530_0744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_content', models.TextField()),
            ],
        ),
    ]
