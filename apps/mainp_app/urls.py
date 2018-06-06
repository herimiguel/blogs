from django.conf.urls import url, include
from . import views 



urlpatterns = [
    url(r'^$', views.index),
    url(r'^blogs$', views.blogs),
    url(r'^comments/(?P<id>\d+)$', views.comments)
]
