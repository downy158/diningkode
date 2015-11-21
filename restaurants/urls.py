from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^rating/(?P<value>[0-9])/$', views.rating, name='rating'),
    url(r'^(?P<name>.+)/$', views.detail, name='detail'),
]
