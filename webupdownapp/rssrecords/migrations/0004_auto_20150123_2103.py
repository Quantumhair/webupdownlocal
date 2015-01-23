# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0003_rssrecord_upordown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssrecord',
            name='url',
            field=models.CharField(max_length=250),
            preserve_default=True,
        ),
    ]
