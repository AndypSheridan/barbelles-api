from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from .serializers import FavouriteSerializer
from .models import Favourite


class FavouriteList(generics.ListCreateAPIView):
    """
    Lists all favourites. If authenticated, User can create a favourite.
    Perform_create links favourite to current logged in User
    """
    serializer_class = FavouriteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favourite.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FavouriteDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieves or destroys a favourite
    Update view not necessary
    """
    serializer_class = FavouriteSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Favourite.objects.all()

