from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, filters
from django.db.models import Count
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import TutorialSerializer
from .models import Tutorial


# Adapted from CI DRF-API walkthrough.
class TutorialList(generics.ListCreateAPIView):
    """
    Retrieve and create new tutorials.
    """
    serializer_class = TutorialSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Tutorial.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
        tutorial_comments_count=Count('tutorialcomment', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # Get tutorials favourited by specific User
        'favourites__owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'favourites_count',
        'tutorial_comments_count',
        'favourites__created_at',
    ]

    def perform_create(self, serializer):
        """
        Add tutorial to database if
        user is logged in and authenticated.
        """
        serializer.save(owner=self.request.user)


class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit or delete tutorial.
    """
    serializer_class = TutorialSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tutorial.objects.annotate(
        favourites_count=Count('favourites', distinct=True),
        tutorial_comments_count=Count('tutorialcomment', distinct=True),
    ).order_by('-created_at')
