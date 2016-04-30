# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usertwitter', '0002_auto_20160430_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='dispositivom',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
