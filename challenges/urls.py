from django.urls import path

from . import views #from same directory import views

urlpatterns = [
    path("january", views.index)
]