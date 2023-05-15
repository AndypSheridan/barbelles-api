from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .serializers import FollowerSerializer
from .models import Follower


class FollowerList(generics.ListCreateAPIView):

    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FolowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or destroys a 'follow'
    Update view not necessary
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
