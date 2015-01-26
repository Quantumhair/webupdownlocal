# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0006_auto_20150126_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssrecord',
            name='url',
            field=models.URLField(max_length=250),
            preserve_default=True,
        ),
    ]
