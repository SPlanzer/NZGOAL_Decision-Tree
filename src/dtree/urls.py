from django.conf import settings
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.global_settings import STATICFILES_DIRS
from . import views

app_name = 'dtree'

urlpatterns = [
    url(r'^about/$', views.about, name = 'about'),
    url(r'datasets/$|^$', views.datasets, name = 'datasets'),
    url(r'^(?P<dataSet_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<dataSet_id>[0-9]+)/addldsid/$', views.addLdsId, name = 'addldsid'),
    url(r'^(?P<dataSet_id>[0-9]+)/remove/$', views.removeDataSet, name = 'remove'),
    url(r'^create_dataset/$', views.createDataSet, name='createdataset'),
    url(r'^audit/$', views.audit, name='audit'),
    url(r'yes/$', views.uDecision, name='yes'),
    url(r'no/$', views.uDecision, name='no'),
    url(r'ok/$', views.uDecision, name='ok'),
    
    #surl(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATICFILES_DIRS}),
]
# #ths is to ensure we dont go live with this statis set up
#if settings.DEBUG:
#urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
#     urlpatterns += patterns('',
#             (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
#     )
#     

    