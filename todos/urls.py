from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^details/(?P<id>\w{0,50})/$', views.details, name='details'),
        url(r'^add/(?P<id>\w{0,50})/$', views.add, name='add'),
        ]
