from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodbounty.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^front', include('front.urls', namespace="front")),
    url(r'^bounty', include('bounty.urls', namespace="bounty")),
    url(r'', include('front.urls', namespace="front")),

)
