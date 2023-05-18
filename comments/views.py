from .serializers import CommentSerializer, CommentDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import Comment


class CommentList(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    filter_backends = [DjangoFilterBackend]

    filterset_fields = [
        'post',
    ]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
