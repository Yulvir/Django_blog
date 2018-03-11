# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20180304_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='option_a',
        ),
        migrations.RemoveField(
            model_name='post',
            name='option_b',
        ),
        migrations.RemoveField(
            model_name='post',
            name='option_c',
        ),
    ]
