from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('input_form', views.input_form, name = "input"),
    path('moteltest', views.modeltest, name = 'moteltest'),
]