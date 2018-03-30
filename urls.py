from django.contrib import admin
from django.conf.urls import include,url
from .import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    #homeapp_detail_view_url
    url(r'^(?P<pk>[0-9]+)/$',views.LocationView.as_view(),name='property'),
    #homeapp/detailview/moredetailview
    url(r'^([0-9]+)/(?P<pk>[0-9]+)/$',views.PropertyView.as_view(),name='propertyview'),

]

    