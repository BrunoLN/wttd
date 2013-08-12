from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^inscricao/', include('eventex.subscriptions.urls',
                                namespace='subscriptions')),
    url(r'', include('eventex.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    (r'^static/(.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT
    }),
)
