from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^rest/v1/incident/(?P<incident_id>\d+)/$', 'webapp.views.incident_update'),
    url(r'^rest/v1/incident/$', 'webapp.views.incident_create'),
    url(r'^rest/v1/incident/all/(?P<incident_id>\d+)/$', 'webapp.views.incident_get'),
    url(r'^rest/v1/incident/tags/(?P<incident_id>\d+)/$', 'webapp.views.incident_gettags'),
    url(r'^rest/v1/incident/updates/(?P<incident_id>\d+)/$', 'webapp.views.incident_getupdates'),
    url(r'^rest/v1/incident/owner/(?P<incident_id>\d+)/$', 'webapp.views.incident_getowner'),
    url(r'^rest/v1/incident/service/(?P<incident_id>\d+)/$', 'webapp.views.incident_getservice'),
    url(r'^rest/v1/tags/$', 'webapp.views.tags_get'),
    url(r'^rest/v1/tag/by-id/(?P<tag_id>\d+)/$', 'webapp.views.tags_get_by_id'),
    url(r'^rest/v1/tag/by-name/(?P<tag_id>\s+)/$', 'webapp.views.tags_get_by_name'),
    url(r'^rest/v1/tag/by-name-fuzzy/(?P<tag_id>\s+)/$', 'webapp.views.tags_get_by_name_fuzzy'),
    url(r'^rest/v1/tag/add/(?P<incident_id>\d+)/$', 'webapp.views.tag_create'),
    url(r'^rest/v1/tag/update/(?P<tag_id>\d+)/$', 'webapp.views.tag_update'),
    url(r'^rest/v1/owner/create/(?P<tag_id>\d+)/$', 'webapp.views.owner_create'),
    url(r'^rest/v1/service/create/(?P<tag_id>\d+)/$', 'webapp.views.service_create'),
    # Examples:
    # url(r'^$', 'outagetrkr.views.home', name='home'),
    # url(r'^outagetrkr/', include('outagetrkr.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

