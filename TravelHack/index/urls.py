from django.conf.urls import url

from . import views

app_name = 'index'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.second, name='second'),
]       