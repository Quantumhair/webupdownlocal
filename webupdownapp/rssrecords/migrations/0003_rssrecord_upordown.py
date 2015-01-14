# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0002_rssrecord_last_checked'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssrecord',
            name='upordown',
            field=models.CharField(default=b'not yet checked', max_length=15),
            preserve_default=True,
        ),
    ]
