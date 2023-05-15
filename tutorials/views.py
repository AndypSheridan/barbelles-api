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
    queryset = Tutorial.objects.all()

    def perform_create(self, serializer):
        serializer.save(owener=self.request.user)


class TutorialDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TutorialSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Tutorial.objects.all()