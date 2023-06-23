from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, CommentDetailSerializer
from .models import Comment

# Class adapted from CI DRF-API walkthrough.
class CommentList(generics.ListCreateAPIView):
    """
    Create and retrieve comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        """
        Save comment.
        """
        serializer.save(owner=self.request.user)

    filter_backends = [DjangoFilterBackend]

    # Show all comments associated with a given post
    filterset_fields = [
        'post',
    ]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, edit or delete comment.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
