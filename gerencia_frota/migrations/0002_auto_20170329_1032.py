# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-29 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia_frota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMarca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Marca_veiculo',
            new_name='Marcaveiculo',
        ),
        migrations.RenameModel(
            old_name='Tipo_Veiculo',
            new_name='TipoVeiculo',
        ),
        migrations.RemoveField(
            model_name='tipo_marca',
            name='id_marca',
        ),
        migrations.RemoveField(
            model_name='tipo_marca',
            name='id_tipo',
        ),
        migrations.DeleteModel(
            name='Tipo_Marca',
        ),
        migrations.AddField(
            model_name='tipomarca',
            name='id_marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencia_frota.Marcaveiculo', verbose_name='MarcaVeiculo'),
        ),
        migrations.AddField(
            model_name='tipomarca',
            name='id_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gerencia_frota.TipoVeiculo', verbose_name='TipoVeiculo'),
        ),
    ]
