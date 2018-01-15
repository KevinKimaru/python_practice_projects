# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-09 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import self_group.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Groupday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('is_merrygoround_registration', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Main_group_fines_interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_interest', models.CharField(max_length=100)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
            ],
        ),
        migrations.CreateModel(
            name='Main_group_loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
            ],
        ),
        migrations.CreateModel(
            name='Main_group_loan_proress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[(1, 1), (2, 2), (3, 3)], max_length=1)),
                ('has_paid_interest', models.BooleanField()),
                ('has_paid_all', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Main_group_loan')),
            ],
        ),
        migrations.CreateModel(
            name='Main_group_merrygoround',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_paid', models.BooleanField(default=True)),
                ('has_won', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
            ],
        ),
        migrations.CreateModel(
            name='Main_group_total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_joined', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_paid', models.BooleanField(default=True)),
                ('amount', models.PositiveIntegerField(blank=True, null=True)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Unga_fines_interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_interest_amount', models.CharField(max_length=200)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Unga_loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Unga_loan_progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(choices=[(1, 1), (2, 2), (3, 3)], max_length=1)),
                ('has_paid_interest', models.BooleanField()),
                ('has_paid_all', models.BooleanField(default=False)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Groupday')),
                ('loan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Unga_loan')),
            ],
        ),
        migrations.CreateModel(
            name='Unga_total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_amount', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='main_group_merrygoround',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member'),
        ),
        migrations.AddField(
            model_name='main_group_loan',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member'),
        ),
        migrations.AddField(
            model_name='main_group_fines_interest',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='self_group.Member'),
        ),
    ]