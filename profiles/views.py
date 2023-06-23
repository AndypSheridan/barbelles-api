from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from django.db.models import Count
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    """
    Serializer for Profile Model.
    Lists all created profiles.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        #  Retrieve a profile's followers
        'owner__following__followed__profile',
        #  Retrieve all profiles followed by a profile, given its id
        'owner__followed__owner__profile'
    ]

    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]

# Class based on CI DRF-API walkthrough.
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update Profile fields if Owner.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
