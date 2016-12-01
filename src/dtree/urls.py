from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import views

app_name = 'dtree'

urlpatterns = [
    url(r'^login_user/$', views.loginUser, name='loginUser'), 
    url(r'^logout_user/$', views.logoutUser, name='logoutUser'),
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
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)