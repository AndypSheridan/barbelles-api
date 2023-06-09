from django.contrib.auth.models import User
from posts.models import Post
from django.db import models


class Comment(models.Model):
    """
    Comment model allows user to comment on posts and workouts
    Related to User, Post and Workout
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
