# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertwitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='namigos',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nfavoritos',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='nseguidores',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='ntweetsp',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
