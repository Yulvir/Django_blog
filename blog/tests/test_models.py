from django.test import TestCase

# Create your tests here.

from blog.models import Post, Comment
from time import sleep
from django.contrib.auth.models import User



class ModelsTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods

        self.user = User.objects.create(username='testuser',
                                        password='12345',
                                        is_active=True,
                                        is_staff=False,
                                        is_superuser=False)
        self.user.save()


    def test_comment(self):
        post = Post.objects.create(title='Big', question='Bob', author=self.user)
        post.publish()
        comment = Comment.objects.create(post=post, author=self.user.username, text="Text")
        comment.approve()
        comment = Comment.objects.get(post=post)
        self.assertEqual(comment.approved_comment, True)

    def test_post_text_label(self):
        post = Post.objects.create(title='Big', question='Bob', author=self.user)
        post.publish()
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('question').verbose_name
        self.assertEquals(field_label, 'question')

    def test_post_title_label(self):
        post = Post.objects.create(title='Big', question='Bob', author=self.user)
        post.publish()
        post = Post.objects.get(pk=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_post_text_length(self):
        post = Post.objects.create(title='Big', question='Bob', author=self.user)
        post.publish()
        post = Post.objects.get(pk=1)
        max_length = post._meta.get_field('question').max_length
        self.assertEquals(max_length, 140)
