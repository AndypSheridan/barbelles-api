from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import TutorialCommentSerializer, TutorialCommentDetailSerializer
from .models import TutorialComment


# Class adapted from CI DRF-API walkthrough.
class TutorialCommentList(generics.ListCreateAPIView):
    """
    Create and retrieve comments.
    """
    serializer_class = TutorialCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TutorialComment.objects.all()

    def perform_create(self, serializer):
        """
        Save comment to user details if user is authenticated.
        """
        serializer.save(owner=self.request.user)

    filter_backends = [DjangoFilterBackend]

    # Show all tutorial comments associated with a given tutorial
    filterset_fields = [
        'tutorial',
    ]


class TutorialCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit or delete comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TutorialCommentDetailSerializer
    queryset = TutorialComment.objects.all()
