from django.urls import path, include

from MyMusicApp.common import views

urlpatterns = [
    path('', views.home, name='home')
]