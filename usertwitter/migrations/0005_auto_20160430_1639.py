# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertwitter', '0004_auto_20160430_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='coordenadas',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='descripcion',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='localidad',
            field=models.CharField(max_length=40, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='login',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
