# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text',
        ),
        migrations.AddField(
            model_name='post',
            name='option_a',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='option_b',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='option_c',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='question',
            field=models.TextField(default=1, max_length=140),
            preserve_default=False,
        ),
    ]
