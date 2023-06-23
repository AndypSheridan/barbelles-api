from rest_framework import serializers
from django.db import IntegrityError
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for Like Model.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id', 'owner', 'post', 'created_at',
        ]

    def create(self, validated_data):
        """
        Displays an error message if the user
        tries to like a post more than once.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate like'}
                )
