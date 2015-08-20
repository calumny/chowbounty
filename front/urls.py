from django.conf.urls import patterns, url

from front import views

urlpatterns = [
    url(r'register/$', views.register, name='register'),
    url(r'login/$', views.login_form, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'$', views.index, name='index'),
]