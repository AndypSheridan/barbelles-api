from .serializers import TutorialCommentSerializer, TutorialCommentDetailSerializer
from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .models import TutorialComment


class TutorialCommentList(generics.ListCreateAPIView):

    serializer_class = TutorialCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = TutorialComment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TutorialCommentDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = TutorialCommentDetailSerializer
    queryset = TutorialComment.objects.all()
