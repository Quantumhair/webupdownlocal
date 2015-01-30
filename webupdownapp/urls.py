from django.conf.urls import patterns, include, url
from django.contrib import admin
from accounts.views import AccountList
from accounts.urls import account_urls
from rssrecords.views import RssRecordList
from rssrecords.views import RssUpList
from rssrecords.views import RssDownList
from rssrecords.views import RssNotCheckedList
from rssrecords.urls import rssrecords_urls
from rssrecords.views import Rss_Seven_Days
from rssrecords.views import Rss_Seven_To_Fourteen
from rssrecords.views import Rss_Over_Fourteen

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
    url(r'^rssrecords/upload/$',
    'webupdownapp.rssrecords.views.rssrecord_upload', name='rssrecord_upload'
    ),
    url(r'^rssrecords/list/$',
        RssRecordList.as_view(), name='rssrecords_list'
    ),
    url(r'^rssrecords/up/$',
        RssUpList.as_view(), name='rssup_list'
    ),
    url(r'^rssrecords/down/$',
        RssDownList.as_view(), name='rssdown_list'
    ),
    url(r'^rssrecords/sevendays/$',
        Rss_Seven_Days.as_view(), name='rss_seven_days.html'
    ),
    url(r'^rssrecords/seventofourteen/$',
        Rss_Seven_To_Fourteen.as_view(), name='rss_seven_to_fourteen.html'
    ),
    url(r'^rssrecords/overfourteen/$',
        Rss_Over_Fourteen.as_view(), name='rss_over_fourteen.html'
    ),
    url(r'^rssrecords/notchecked/$',
        RssNotCheckedList.as_view(), name='rssnotchecked_list'
    ),
    url(r'^rssrecords/summary/$',
    'webupdownapp.rssrecords.views.rssrecord_summary', name='rssrecords_summary'
    ),
    url(r'^rssrecords/(?P<uuid>[\w-]+)/', include(rssrecords_urls)
    ),

)
