from django.contrib.auth.models import User
from tutorials.models import Tutorial
from django.db import models


class Favourite(models.Model):
    """
    Favourite model used to allow Users to favourite tutorials
    'unique_together' prevents a User from favouriting the 
    same tutorial twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, related_name='favourites', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'tutorial']

    def __str__(self):
        return f'{self.owner} {self.tutorial}'
