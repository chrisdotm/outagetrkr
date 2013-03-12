from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'rest/v1/incident/(?P<incident_id>\d+)/$', 'webapp.views.incident_readupdate'),
    url(r'rest/v1/incident/$', 'webapp.views.incident_create'),
    # Examples:
    # url(r'^$', 'outagetrkr.views.home', name='home'),
    # url(r'^outagetrkr/', include('outagetrkr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

