from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^publishMouseCoords$', views.MouseCoordinates.as_view(),
        name='publishMouseCoords'),
]
