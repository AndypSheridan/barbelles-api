from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='post.owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='post.owner.id')
    profile_image = serializers.ReadOnlyField(source='post.owner.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'title', 'story', 'image', 'created_at', 'updated_at', 'is_owner'
        ]

