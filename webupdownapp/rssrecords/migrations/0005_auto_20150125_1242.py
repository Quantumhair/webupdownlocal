# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0004_auto_20150123_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssrecord',
            name='url',
            field=models.URLField(max_length=250),
            preserve_default=True,
        ),
    ]
