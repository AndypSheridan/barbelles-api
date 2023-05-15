from django.db import models
from django.contrib.auth.models import User
from  embed_video.fields  import  EmbedVideoField


class Tutorial(models.Model):
    """
    Tutorial model, allows site admin
    to embed videos
    Related to User model
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    summary = models.TextField(blank=True)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
