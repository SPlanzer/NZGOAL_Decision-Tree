from django.contrib import admin
from django.conf.urls import url, include
from . import views

app_name = 'dtree'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'datasets', views.datasets, name = 'datasets'),
    url(r'^(?P<dataSet_id>[0-9]+)/$', views.detail, name = 'detail'),
    url(r'^(?P<dataSet_id>[0-9]+)/addldsid/$', views.addLdsId, name = 'addldsid'),
    url(r'^(?P<dataSet_id>[0-9]+)/remove/$', views.removeDataSet, name = 'remove'),
    url(r'^create_dataset/$', views.createDataSet, name='createdataset'),
    url(r'yes/$', views.uDecision, name='yes'),
    url(r'no/$', views.uDecision, name='no'),
    url(r'ok/$', views.uDecision, name='ok'),
]
