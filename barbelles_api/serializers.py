from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    """
    Generate user information to display when user logs in.
    """
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')
    profile_is_staff = serializers.ReadOnlyField(source='profile.is_staff')

    class Meta(UserDetailsSerializer.Meta):
        """
        Fields to display.
        """
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', 'profile_is_staff',
        )
