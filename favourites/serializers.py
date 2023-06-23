from rest_framework import serializers
from django.db import IntegrityError
from .models import Favourite

# Class adapted from CI DRF-API walkthrough.
class FavouriteSerializer(serializers.ModelSerializer):
    """
    Favourite Model serializer.
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Fields to be displayed.
        """
        model = Favourite
        fields = [
            'id', 'owner', 'tutorial', 'created_at',
        ]

    def create(self, validated_data):
        """
        Displays error message if the user tries 
        to like the same post more than once.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError(
                {'detail': 'possible duplicate favourite'}
                )
