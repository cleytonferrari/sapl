# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0034_auto_20160510_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoacessorio',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='Nome'),
        ),
    ]
