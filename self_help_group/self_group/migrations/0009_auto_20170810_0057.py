# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_group', '0008_auto_20170810_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_group_fines_interest',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='unga_fines_interests',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='unga_loan',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
