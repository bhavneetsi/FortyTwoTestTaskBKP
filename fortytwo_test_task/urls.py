from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
from fortytwoapps.views import Index, Requests, UpdateContact
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^requests/', Requests.as_view(), name='requests'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('django.contrib.auth.urls',
                               namespace='accounts')),
    url(r'^updatecontact/(?P<pk>\d+)/$',UpdateContact.as_view(),name='update_contact'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
                        url(r'^uploads/(?P<path>.*)$',
                            'django.views.static.serve',
                            {'document_root': settings.MEDIA_ROOT}))
