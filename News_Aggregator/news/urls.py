from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.articles_list, name='articles_list'),
    url(r'^feeds/new', views.new_feed, name='feed_new'),
    url(r'^feeds/checking', views.feeds_checking, name='feeds_checking'),
    url(r'^feeds/', views.feeds_list, name='feeds_list'),
    url(r'^world/', views.world_list, name='world'),
    url(r'^India/', views.India_list, name='India'),
    url(r'^business/', views.business_list, name='business'),
    url(r'^technology/', views.technology_list, name='technology'),
    url(r'^entertainment/', views.entertainment_list, name='entertainment'),
    url(r'^sports/', views.sports_list, name='sports'),
    url(r'^science/', views.science_list, name='science'),
    url(r'^health/', views.health_list, name='health'),
]
