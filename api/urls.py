from django.conf.urls import patterns, url, include

from rest_framework.authtoken import views
from django.contrib.gis import admin

urlpatterns = [
    url(r'/api-token-auth$', views.obtain_auth_token),
]