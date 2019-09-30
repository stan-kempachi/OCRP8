from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^search/$', views.search, name="search"),
    url(r'^mentionlegal/$', views.mention_legale, name="mention"),
    url(r'^food/(?P<food_id>[0-9]+)/$', views.details, name="details"),
    # url(
    #     r'^food-autocomplete/$',
    #     views.FoodAutocomplete,
    #     name='food-autocomplete',
    # ),
    ]

