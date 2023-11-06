from django.contrib import admin
from .models import City, House, HousePictures, Threshold_price

# Register your models here.

admin.site.register([City, House, HousePictures, Threshold_price])