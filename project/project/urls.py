from django.conf.urls import patterns, include, url
from django.contrib import admin

#from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('website.urls', namespace="website")),
    url(r'^api/', include('api.urls', namespace="api")),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
