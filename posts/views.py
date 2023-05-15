from rest_framework import status, permissions, generics, filters
from barbelles_api.permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from django.db.models import Count
from django.http import Http404
from .models import Post


class PostList(generics.ListCreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True),
    ).order_by('created_at')

    filter_backends = [
        filters.OrderingFilter
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count = Count('likes', distinct=True),
        comments_count = Count('comment', distinct=True),
    ).order_by('created_at')
