# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-04 09:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('morepractice', '0006_auto_20170804_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_accessed',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 4, 12, 28, 22, 203011)),
        ),
    ]