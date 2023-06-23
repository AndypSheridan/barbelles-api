from rest_framework import serializers
from favourites.models import Favourite
from .models import Tutorial


# Adapted from CI DRF-API walkthrough.
class TutorialSerializer(serializers.ModelSerializer):
    """
    Serializer for Tutorial Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()
    tutorial_comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        """
        Return correct user.
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_favourite_id(self, obj):
        """
        Return total favourites.
        """
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, tutorial=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        """
        Fields to display.
        """
        model = Tutorial
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'title', 'summary', 'video', 'created_at',
            'updated_at', 'is_owner', 'favourite_id', 
            'favourites_count', 'tutorial_comments_count',
        ]