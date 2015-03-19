# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rssrecords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssrecord',
            name='last_checked',
            field=models.DateField(default=datetime.date(1970, 1, 1)),
            preserve_default=True,
        ),
    ]
