from django.contrib.auth.models import User
from tutorials.models import Tutorial
from django.db import models


class TutorialComment(models.Model):
    """
    Tutorial cmment model allows user to comment on tutorials
    Related to User, Tutorial
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
