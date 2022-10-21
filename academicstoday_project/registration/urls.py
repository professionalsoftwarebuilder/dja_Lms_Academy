from django.urls import include, path
from . import views

urlpatterns = [
    path('register_modal', views.register_modal),
    path('register', views.register),
]