# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Comment
# Register your models here.
from django.contrib import admin
from .models import Post

admin.site.register(Post)
admin.site.register(Comment)
