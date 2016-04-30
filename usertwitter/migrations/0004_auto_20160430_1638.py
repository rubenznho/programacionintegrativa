# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertwitter', '0003_usuario_dispositivom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=25, null=True, blank=True),
        ),
    ]
