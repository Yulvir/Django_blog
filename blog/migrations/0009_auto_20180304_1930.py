# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180304_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='author',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='post',
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
