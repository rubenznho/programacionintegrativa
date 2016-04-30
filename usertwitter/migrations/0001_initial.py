# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=25)),
                ('login', models.CharField(max_length=25)),
                ('localidad', models.CharField(max_length=40)),
                ('coordenadas', models.CharField(max_length=25)),
                ('descripcion', models.CharField(max_length=250)),
            ],
        ),
    ]
