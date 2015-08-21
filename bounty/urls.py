from django.conf.urls import patterns, url, include

from bounty import views

from django.contrib.gis import admin

urlpatterns = [
    url(r'/admin$', include(admin.site.urls)),
    url(r'/edit_address$', views.edit_address, name='edit_address'),
    url(r'/save_address$', views.save_address, name='save_address'),
    url(r'/add_bounty$', views.add_bounty, name='add_bounty'),
    url(r'/new$', views.new_bounty, name='new_bounty'),
    url(r'/local_bounties$', views.local_bounties, name='local_bounties'),
    url(r'/default_bounties$', views.default_bounties, name='default_bounties'),
    url(r'/rest_bounties_list$', views.rest_bounties_list, name='rest_bounties_list'),
    url(r'/post_bounty$', views.post_bounty, name='post_bounty'),
    url(r'/(?P<bounty_id>.+)$', views.show_bounty, name='show_bounty'),
    url(r'$', views.list_bounties, name='list_bounties'),
]