# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('morepractice', '0002_publish_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publish',
            name='author',
        ),
        migrations.AddField(
            model_name='publish',
            name='writer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='morepractice.Writer'),
        ),
    ]
