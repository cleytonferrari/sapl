# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import materia.models
import sapl.utils


class Migration(migrations.Migration):

    dependencies = [
        ('materia', '0032_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentoacessorio',
            name='texto_original',
            field=models.FileField(blank=True, null=True, upload_to=materia.models.texto_upload_path, validators=[sapl.utils.restringe_tipos_de_arquivo_txt], verbose_name='Texto Integral'),
        ),
    ]
