from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<gazebo_title>[\w-]*)/$', views.experiment, name='experiment'),
]
