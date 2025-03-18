from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, FavSongSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import FavSong

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class FavSongListCreate(generics.ListCreateAPIView):
    serializer_class = FavSongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return FavSong.objects.none()  
        return FavSong.objects.filter(profile_owner=user) 
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(profile_owner=self.request.user)
        else:
            print(serializer.errors)

class FavSongDelete(generics.DestroyAPIView):
    serializer_class = FavSongSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return FavSong.objects.filter(profile_owner=user)