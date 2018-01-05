#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import url
from. import views

app_name ='alarm'
urlpatterns = [
    url(r'^sendMsg/$', views.sendMsg),
    url(r'^login$', views.login),
]