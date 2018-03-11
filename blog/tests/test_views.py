# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User  # Required to assign User as a borrower
from blog.models import Post, Comment
from django.test import TestCase
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

# Delete __init__.py file from the same package as manage.py
# Command to run the tests:  ./manage.py test blog/tests

# Create pycharm config
# 1 - New python config
# 2 - Script: /home/ncarvalho/django_girls/django_girls/manage.py
# 3 - Parameters: test blog/tests


class BlogViewsTest(TestCase):

    def setUp(self):

        # Every test needs access to the request factory.
        self.user = User.objects.create(username='testuser',
                                        password='12345',
                                        is_active=True,
                                        is_staff=False,
                                        is_superuser=False)

        self.user.set_password('hello')
        self.user.save()
        self.user = authenticate(username='testuser', password='hello')
        self.login = self.client.login(username='testuser', password='hello')
        self.post = Post.objects.create(title="Title", question="text", author=self.user)
        self.post.publish()

        self.comment = Comment.objects.create(post=self.post, text="text", author=self.user.username)
        self.comment.approve()

    def test_post_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(200, response.status_code)

    def test_post_detail(self):

        response = self.client.get(reverse('post_detail', args=("testuser", 1)))
        self.assertEqual(200, response.status_code)

    def test_post_new(self):
        response = self.client.get(reverse('post_new', args=("testuser", )))
        self.assertEqual(200, response.status_code)

    def test_post_edit(self):
        response = self.client.get(reverse('post_edit', args=("testuser", 1)))
        self.assertEqual(200, response.status_code)

    def test_post_draft_list(self):
        response = self.client.get(reverse('post_draft_list', args=("testuser", )))
        self.assertEqual(200, response.status_code)

    def test_post_remove(self):
        response = self.client.get(reverse('post_remove', args=("testuser", 1)))
        self.assertEqual(302, response.status_code)

    def test_post_publish(self):
        response = self.client.get(reverse('post_publish', args=("testuser", 1)))
        self.assertEqual(302, response.status_code)

    def test_add_comment_to_post(self):
        response = self.client.get(reverse('add_comment_to_post', args=("testuser", 1)))
        self.assertEqual(200, response.status_code)

    def test_comment_approve(self):
        response = self.client.get(reverse('comment_approve', args=("testuser", 1)))
        self.assertEqual(302, response.status_code)

    def test_comment_remove(self):
        response = self.client.get(reverse('comment_remove', args=("testuser", 1)))
        self.assertEqual(302, response.status_code)

    def test_get_user_profile(self):
        response = self.client.get(reverse('get_user_profile', args=("testuser", )))
        self.assertEqual(200, response.status_code)
