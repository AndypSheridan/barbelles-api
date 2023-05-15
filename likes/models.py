from django.contrib.auth.models import User
from posts.models import Post
from django.db import models


class Like(models.Model):
    """
    Like model used to allow Users to like Posts by other Users
    Also to allow User to like Workouts
    'unique_together' prevents a User from liking the same post twice
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'
