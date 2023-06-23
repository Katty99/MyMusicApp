from django.urls import path

from MyMusicApp.account import views

urlpatterns = [
    path('details/', views.profile_details, name='profile_details'),
    path('delete/', views.profile_delete, name='profile_delete'),
]