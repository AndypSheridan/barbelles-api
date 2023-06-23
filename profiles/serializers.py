from rest_framework import serializers
from followers.models import Follower
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile model.
    Provides readability to profile data in API.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Links user to User profile.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Following count for individual user.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

    class Meta:
        """
        List of Profile Model fields to display.
        """
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio', 'image',
            'created_at', 'updated_at', 'is_owner',
            'following_id', 'posts_count',
            'followers_count', 'following_count',
            'is_staff', 'is_superuser',
        ]
