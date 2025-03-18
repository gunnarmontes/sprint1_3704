from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FavSong


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user


class FavSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavSong
        fields = ["id", "artist", "song_name", "profile_owner"]
        extra_kwargs = {"profile_owner": {"read_only": True}}
