from django.conf.urls import patterns, url

rssrecords_urls = patterns('',

    url(r'^$',
        'webupdownapp.rssrecords.views.rssrecord_detail', name='rssrecord_detail'
    ),
    url(r'^edit/$',
        'webupdownapp.rssrecords.views.rssrecord_cru', name='rssrecord_update'
    ),

)