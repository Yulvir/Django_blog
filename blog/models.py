# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    question = models.TextField(max_length=140)
    numerical_rate = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,
                                          null=True)

    # New
    likes = models.PositiveIntegerField(default=0)

    @property
    def total_likes(self):
        return self.likes.count()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField(max_length=100)
    numerical_rate = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


def approved_comments(self):
    return self.comments.filter(approved_comment=True)