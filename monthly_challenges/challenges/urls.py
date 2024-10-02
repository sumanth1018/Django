from django.urls import path
from . import views

urlpatterns = [
    path("january", views.jan), # tells that if the request is /january the exucutes the index view(function).
    path("febuary", views.feb)
]