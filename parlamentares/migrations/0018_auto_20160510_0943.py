# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parlamentares', '0017_remove_parlamentar_unidade_deliberativa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filiacao',
            options={'ordering': ('parlamentar', '-data', '-data_desfiliacao'), 'verbose_name': 'Filiação', 'verbose_name_plural': 'Filiações'},
        ),
    ]
