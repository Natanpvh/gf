# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_frota', '0002_auto_20170329_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoveiculo',
            name='marca',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='gerencia_frota.Marcaveiculo'),
            preserve_default=False,
        ),
    ]
