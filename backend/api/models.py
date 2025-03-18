from django.db import models
from django.contrib.auth.models import User


class FavSong(models.Model):
    artist = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    profile_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_owner")

    
    def __str__(self):
        return 'Made by: ' + self.artist + 'Name: ' + self.song_name