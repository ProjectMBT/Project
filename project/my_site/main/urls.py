from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index ),
    path('community', views.community),
    path('create', views.create),
    path('join', views.join),
    path('join', views.login),
]
