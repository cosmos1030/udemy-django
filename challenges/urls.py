from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("<int:month>", views.num_month),
    path("<str:month>", views.month),
    
]