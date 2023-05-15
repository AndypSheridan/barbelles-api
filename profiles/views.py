from rest_framework import generics, permissions, filters
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from django.db.models import Count
from django.http import Http404
from .models import Profile


class ProfileList(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
