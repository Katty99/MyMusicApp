from django.urls import path, include

from MyMusicApp.albums import views

urlpatterns = [
    path('add/', views.add_album, name='add_album'),
    path('details/<int:pk>/', views.details_album, name='details_album'),
    path('edit/<int:pk>/', views.edit_album, name='edit_album'),
    path('delete/<int:pk>/', views.delete_album, name='delete_album'),
]