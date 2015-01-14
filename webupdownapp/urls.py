from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import AccountList
from accounts.urls import account_urls
from rssrecords.views import RssRecordList
from rssrecords.urls import rssrecords_urls

admin.autodiscover()

from marketing.views import HomePage

urlpatterns = patterns('',

    # Marketing pages
    url(r'^$', HomePage.as_view(), name="home"),

    # Subscriber related URLs
    url(r'^signup/$',
        'webupdownapp.subscribers.views.subscriber_new', name='sub_new'
    ),


    # Admin URL
    (r'^admin/', include(admin.site.urls)),
	

    # Login/Logout URLs
    (r'^login/$',
    	'django.contrib.auth.views.login', {'template_name': 'login.html'}
    ),
    (r'^logout/$',
    	'django.contrib.auth.views.logout', {'next_page': '/login/'}
    ),

    # Account related URLs
    url(r'^account/new/$',
    'webupdownapp.accounts.views.account_cru', name='account_new'
    ),
    url(r'^account/list/$',
        AccountList.as_view(), name='account_list'
    ),
    url(r'^account/(?P<uuid>[\w-]+)/', include(account_urls)),

    # Contact related URLS


    # Communication related URLs

    # RSS records related URLs
    url(r'^rssrecords/new/$',
    'webupdownapp.rssrecords.views.rssrecord_cru', name='rssrecord_new'
    ),
    url(r'^rssrecords/list/$',
        RssRecordList.as_view(), name='rssrecords_list'
    ),
    url(r'^rssrecords/(?P<uuid>[\w-]+)/', include(rssrecords_urls)
    ),

)
