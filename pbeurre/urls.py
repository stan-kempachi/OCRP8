from django.conf.urls import url
from django.contrib import admin
from dal import autocomplete
from pbeurre.views import FoodAutocomplete

from pbeurre.models import Food
from pbeurre.forms import FoodForm

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^$', views.FoodAutocomplete, name='food-autocomplete'),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^register/$', views.register_view, name="register"),
    url(r'^logout/$', views.logout_view, name="logout"),
    url(r'^search/$', views.search, name="search"),
    url(r'^moncompte/$', views.mon_compte, name="mon_compte"),
    url(r'^mentionlegal/$', views.mention_legale, name="mention"),
    url(r'^food/(?P<food_id>[0-9]+)/$', views.details, name="details"),
    url(r'^content/', admin.site.urls, name="admin"),
    url(r'^addfavorite/(?P<food_id>[0-9]+)/$', views.add_favorite, name="add_favorite"),
    url(r'^favorite/$', views.favorite, name='favorite')
]