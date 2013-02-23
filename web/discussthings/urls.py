from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
                       # ex: /things/
                       url(r'^$', views.index, name='index'),
                       # ex: /things/3/
                       url(r'^(?P<thing_id>\d+)/$', views.thing, name='thing'),
                       url(r'^thingify/$', views.thingifier, name='thingifier'),
                       url(r'^(?P<thing_id>\d+)/talk/$', views.talk, name='talk'),
                       url(r'^(?P<thing_id>\d+)/(?P<topic_id>\d+)/reply/$', views.reply, name='reply'),
                       url(r'^discussthings/static/thing_pictures/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'discussthings/static/thing_pictures'})
)
