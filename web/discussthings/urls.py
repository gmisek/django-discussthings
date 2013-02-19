from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       # ex: /things/
                       url(r'^$', views.index, name='index'),
                       # ex: /things/3/
                       url(r'^(?P<thing_id>\d+)/$', views.thing, name='thing'),
                       url(r'^thingify/(?P<thing_id>\d+)/$', views.thingifier, name='thingifier'),
                       url(r'^(?P<thing_id>\d+)/talk/$', views.talk, name='talk'),
                       url(r'^(?P<thing_id>\d+)/reply/(?P<topic_id>\d+)/$', views.reply, name='reply'),
)
