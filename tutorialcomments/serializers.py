from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import TutorialComment


class TutorialCommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

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

