from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to User instance
    Allows users to add posts with images
    Default image allows reference of image.url
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    story = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_eirfz0', blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id}{self.title}'
