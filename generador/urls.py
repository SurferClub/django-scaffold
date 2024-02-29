
from django.urls import path 
from .views import home, generate


urlpatterns = [
    path("", home , name="home"),
    path("password", generate,name="generate")
]