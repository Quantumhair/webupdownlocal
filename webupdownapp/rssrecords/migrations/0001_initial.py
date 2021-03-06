# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import shortuuidfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rssrecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', shortuuidfield.fields.ShortUUIDField(unique=True, max_length=22, editable=False, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=250)),
                ('desc', models.TextField(blank=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('last_checked', models.DateField(default=datetime.date(1970, 1, 1), auto_now=True)),
                ('upordown', models.CharField(default=b'not yet checked', max_length=15)),
                ('dayssinceupdate', models.IntegerField(default=9999)),
                ('group', models.CharField(default=b'No Group', max_length=100)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'rssrecords',
            },
            bases=(models.Model,),
        ),
    ]
