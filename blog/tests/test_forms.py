from django.test import TestCase

# Create your tests here.
from blog.forms import CommentForm, PostForm
from django.contrib.auth.models import User


class FormsTest(TestCase):

    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods

        self.user = User.objects.create(username='testuser',
                                        password='12345',
                                        is_active=True,
                                        is_staff=False,
                                        is_superuser=False)
        self.user.save()

    def test_post_form(self):
        form_data = {'question': "text", "title": "title"}
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form(self):
        form_data = {'author': "autor", 'text': "text"}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())