# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180304_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='options',
        ),
    ]
