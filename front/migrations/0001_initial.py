# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 18:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField()),
                ('end_date', models.DateField()),
                ('destination', models.CharField(max_length=50)),
                ('product_id', models.PositiveIntegerField()),
                ('insured_cpf', models.CharField(max_length=14)),
                ('insured_name', models.CharField(max_length=100)),
                ('insured_birth', models.DateField()),
                ('card_name', models.CharField(max_length=100)),
                ('card_cpf', models.CharField(max_length=14)),
                ('card_number', models.CharField(max_length=16)),
                ('card_mouth', models.CharField(max_length=2)),
                ('card_year', models.CharField(max_length=4)),
                ('card_cvv', models.CharField(max_length=4)),
                ('buy_name', models.CharField(max_length=100)),
                ('buy_email', models.CharField(max_length=100)),
                ('buy_phone', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ('pk',),
            },
        ),
    ]
