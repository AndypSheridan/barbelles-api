from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Adapted from CI DRF-API walkthrough.
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        """
        Link comment to user ID.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Display time elapsed since comment created.
        """
        return naturaltime(obj.updated_at)

    def get_is_owner(self, obj):
        """
        Display time since comment created.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Fields to display.
        """
        model = Comment
        fields = [
            'id', 'owner', 'content', 'profile_id',
            'profile_image', 'post', 'created_at',
            'updated_at', 'is_owner',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for Comment detail view.
    """
    post = serializers.ReadOnlyField(source='post.id')
