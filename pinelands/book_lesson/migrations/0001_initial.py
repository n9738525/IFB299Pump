# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-29 17:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Instrument', models.CharField(max_length=128)),
                ('Language', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('FirstName', models.CharField(max_length=128)),
                ('LastName', models.CharField(max_length=128)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=128)),
                ('phonenumber', models.CharField(max_length=128)),
                ('facebookID', models.URLField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('FirstName', models.CharField(max_length=128)),
                ('LastName', models.CharField(max_length=128)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=128)),
                ('phonenumber', models.CharField(max_length=128)),
                ('facebookID', models.URLField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('FirstName', models.CharField(max_length=128)),
                ('LastName', models.CharField(max_length=128)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('OTHER', 'Other')], max_length=128)),
                ('phonenumber', models.CharField(max_length=128)),
                ('LanguagesKnown', models.CharField(max_length=128)),
                ('qualifications', models.TextField()),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='Student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_lesson.Student'),
        ),
        migrations.AddField(
            model_name='lesson',
            name='Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book_lesson.Teacher'),
        ),
    ]
