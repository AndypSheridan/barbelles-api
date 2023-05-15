from rest_framework import status, generics, permissions
from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.views import APIView
from django.http import Http404
from .models import Profile


class ProfileList(generics.ListAPIView):

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    # def get(self, request):
    #     profiles = Profile.objects.all()
    #     serializer = ProfileSerializer(
    #         profiles, many=True, context={'request': request}
    #         )
    #     return Response(serializer.data)


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()

    # def get_object(self, pk):
    #     try:
    #         profile = Profile.objects.get(pk=pk)
    #         self.check_object_permissions(self.request, profile)
    #         return profile
    #     except Profile.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(
    #         profile, context={'request': request}
    #         )
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     profile = self.get_object(pk)
    #     serializer = ProfileSerializer(
    #         profile, data=request.data, context={'request': request}
    #         )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
