from django.db import models
from django.contrib.auth.models import User
from datetime import date

from shortuuidfield import ShortUUIDField


class Rssrecord(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=250)
    desc = models.TextField(blank=True)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)
    last_checked = models.DateField(auto_now=False, default=date(1970,01,01))
    upordown = models.CharField(max_length=15, default='not yet checked')
    dayssinceupdate = models.IntegerField(default=9999)
    group = models.CharField(max_length=100, default='No Group')

    class Meta:
        verbose_name_plural = 'rssrecords'

    def __unicode__(self):
        return u"%s" % self.url

    @models.permalink
    def get_absolute_url(self):
        return 'rssrecord_detail', [self.uuid]

    @models.permalink
    def get_update_url(self):
        return 'rssrecord_update', [self.uuid]

    @models.permalink
    def get_delete_url(self):
        return 'rssrecord_delete', [self.uuid]

