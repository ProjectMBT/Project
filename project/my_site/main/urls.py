from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index ),
    path('community', views.community),
    path('create', views.create),
    path('join', views.join),
    path('login', views.login),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
