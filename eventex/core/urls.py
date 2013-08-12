# coding: utf-8
from django.conf.urls import patterns, url


urlpatterns = patterns(
    'eventex.core.views',
    url(r'^$', 'homepage', name='homepage'),
)
