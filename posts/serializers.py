from rest_framework import serializers
from likes.models import Like
from .models import Post


# Class adapted from CI DRF-API walkthrough.
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """
        Restricts image sizes.
        """
        if value.size > 1024 * 1024 * 3:
            raise serializers.ValidationError(
                'Image size larger than 3MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        """
        Return total number of likes on post.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        """
        Fields to be displayed.
        """
        model = Post
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'title', 'story', 'image', 'image_filter',
            'created_at', 'updated_at', 'is_owner',
            'like_id', 'likes_count', 'comments_count',
        ]
