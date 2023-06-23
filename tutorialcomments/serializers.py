from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import TutorialComment


# Class adapted from CI DRF-API walkthrough.
class TutorialCommentSerializer(serializers.ModelSerializer):
    """
    Serializer for TutorialComment Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        """
        Display time elapsed since comment created.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Display time since comment edited.
        """
        return naturaltime(obj.updated_at)

    def get_is_owner(self, obj):
        """
        Link comment to user.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        """
        Fields to display.
        """
        model = TutorialComment
        fields = [
            'id', 'owner', 'content', 'profile_id',
            'profile_image', 'tutorial', 'created_at',
            'updated_at', 'is_owner',
        ]


class TutorialCommentDetailSerializer(TutorialCommentSerializer):
    """
    Serializer for detail view.
    """
    tutorial = serializers.ReadOnlyField(source='tutorial.id')
