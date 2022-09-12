from django.contrib import admin
from .models import *

admin.site.register(RateStars)

admin.site.site_url = "/ega/"