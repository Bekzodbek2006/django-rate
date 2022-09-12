from .views import *
from django.urls import path 

app_name = "app"

urlpatterns = [
    path('', home, name="home"),
    path('rate-image/', rateImg, name="rate_img")
]
