from favourites.models import Favourite
from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    favourite_id = serializers.SerializerMethodField()
    favourites_count = serializers.ReadOnlyField()
    tutorial_comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_favourite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favourite = Favourite.objects.filter(
                owner=user, tutorial=obj
            ).first()
            return favourite.id if favourite else None
        return None

    class Meta:
        model = Tutorial
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'title', 'summary', 'video', 'created_at',
            'updated_at', 'is_owner', 'favourite_id', 
            'favourites_count', 'tutorial_comments_count',
        ]