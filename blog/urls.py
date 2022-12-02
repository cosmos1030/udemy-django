from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='start-page'),
    path('posts', views.posts, name='posts-page'),
    path('posts/<slug:slug>', views.detail, name='detail-page'),
]
