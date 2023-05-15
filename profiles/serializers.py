from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'bio', 'image',
            'created_at', 'updated_at', 'is_owner', 
            'following_id',
        ]
