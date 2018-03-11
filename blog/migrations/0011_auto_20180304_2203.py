# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180304_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='numerical_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='numerical_rate',
            field=models.IntegerField(default=0),
        ),
    ]
