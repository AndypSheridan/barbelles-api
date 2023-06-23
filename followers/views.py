from rest_framework import generics, permissions
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import FollowerSerializer
from .models import Follower


class FollowerList(generics.ListCreateAPIView):
    """
    Allows user to follow another user.
    """
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        """
        If a user is authenticated, follow
        request is saved to database.
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or destroys a 'follow'
    Update view not necessary.
    """
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
