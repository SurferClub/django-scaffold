
from django.urls import path 
from .views import cajero, detailView


urlpatterns = [
    path("caja", cajero , name='caja' ),
    path("details", detailView, name="detail")
]