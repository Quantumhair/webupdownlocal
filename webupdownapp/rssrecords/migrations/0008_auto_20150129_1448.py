# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0007_auto_20150126_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='rssrecord',
            name='dayssinceupdate',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rssrecord',
            name='group',
            field=models.CharField(default=b'No Group', max_length=100),
            preserve_default=True,
        ),
    ]
