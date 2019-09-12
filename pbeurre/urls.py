from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^search/$', views.search, name="search"),
    url(r'^mentionlegal/$', views.mention_legale, name="mention"),
    url(r'^404/$', views.page_not_found, name="404"),
    url(r'^details/$', views.details, name="details")
    ]
