from rest_framework import serializers
from .models import TutorialComment


class TutorialCommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = TutorialComment
        fields = [
            'id', 'owner', 'content', 'profile_id',
            'profile_image', 'tutorial', 'created_at',
            'updated_at', 'is_owner',
        ]


class TutorialCommentDetailSerializer(TutorialCommentSerializer):

    tutorial = serializers.ReadOnlyField(source='tutorial.id')

