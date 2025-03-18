from django.urls import path
from . import views

urlpatterns = [
    path("favsongs/", views.FavSongListCreate.as_view(), name="favsong-list"),
    path("favsongs/delete/<int:pk>/", views.FavSongDelete.as_view(), name="delete-song")
]