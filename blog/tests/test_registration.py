# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.contrib.auth.models import User  # Required to assign User as a borrower
from blog.models import Post, Comment

# Delete __init__.py file from the same package as manage.py
# Command to run the tests:  ./manage.py test blog/tests

from django.test import Client


class RegistrationTest(TestCase):


    def test_login(self):

        c = Client()
        response = c.post('/accounts/login/?next=/', {'username': 'ncarvalho', 'password': 'melides67'})
        self.assertEqual(response.status_code, 200)

    def test_signup(self):

        c = Client()
        response = c.post('/signup/', {'username': 'test_signup_user', 'password1': '123456', 'password2': '123456'})
        # Code 302 Url redirection
        self.assertEqual(response.status_code, 302)






