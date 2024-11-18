from django.contrib import admin
from .models import RequestData, StoreData, RequestAdress, StoreAdress

# Register your models here.
admin.site.register([RequestData, StoreData, RequestAdress, StoreAdress])