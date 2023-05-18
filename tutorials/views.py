from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, generics, filters
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import TutorialSerializer
from django.db.models import Count
from django.http import Http404
from .models import Tutorial


class TutorialList(generics.ListCreateAPIView):

    serializer_class = TutorialSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Tutorial.objects.annotate(
        favourites_count = Count('favourites', distinct=True),
        tutorial_comments_count = Count('tutorialcomment', distinct=True),
    ).order_by('created_at')

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
        serializer.save(owner=self.request.user)


class TutorialDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TutorialSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tutorial.objects.annotate(
        favourites_count = Count('favourites', distinct=True),
        tutorial_comments_count = Count('tutorialcomment', distinct=True),
    ).order_by('created_at')