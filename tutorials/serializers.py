from rest_framework import serializers
from .models import Tutorial


class TutorialSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Tutorial
        fields = [
            'id', 'owner', 'profile_id', 'profile_image',
            'title', 'summary', 'video', 'created_at',
            'updated_at', 'is_owner',
        ]