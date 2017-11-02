# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-01 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ambientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('nro_personas', models.PositiveIntegerField(default=1, help_text='Debe incluir a la person')),
                ('fecha', models.DateTimeField()),
                ('detalle', models.TextField(blank=True, default=None, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambientes.Mesa')),
            ],
        ),
    ]
