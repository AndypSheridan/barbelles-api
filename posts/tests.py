from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create(username='admin',password='testpasswordadmin')

    def test_can_list_posts(self):
        admin = User.objects.get(username='admin')
        Post.objects.create(owner=admin, title='Tennis team')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
