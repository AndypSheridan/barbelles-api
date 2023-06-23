from rest_framework import permissions, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
from barbelles_api.permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from .models import Post


# Class adapted from CI DRF-API walkthrough.
class PostList(generics.ListCreateAPIView):
    """
    Retrieve and create new posts.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        # User feed shows posts from Users being followed
        'owner__followed__owner__profile',
        # Get posts liked by current User
        'likes__owner__profile',
        # Get posts owned by specific User
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
    ]

    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        """
        If user is logged in, saves
        new post to database.
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Function to retrieve, edit or
    delete post if owner.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('created_at')
