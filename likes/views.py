from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .serializers import LikeSerializer
from .models import Like


class LikeList(generics.ListCreateAPIView):
    """
    Lists all likes. If authenticated, User can create a like.
    Perform_create links like to current logged in User
    """
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or destroys a like
    Update view not necessary
    """
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Like.objects.all()
