from django.conf.urls import patterns, include, url
from django.contrib import admin
from Stel import settings
import api

admin.autodiscover()

urlpatterns = patterns('',
     url(r'^$', 'anagrafica.views.home', name='home'),
     url(r'^api/get_str/(?P<classe>.*)/(?P<id>.*)/$', api.get_str ),
     url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/js' % settings.PROJECT_ROOT,'show_indexes':True}),
     url(r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/css' % settings.PROJECT_ROOT,'show_indexes':True}),
     url(r'^dato/(?P<dato>\d+)/$', 'anagrafica.views.guarda'),
     url(r'^test/$', 'anagrafica.views.download_pdf'),    
     url(r'^admin/', include(admin.site.urls)),
)

