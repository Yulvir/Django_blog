# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rating',
            name='ratings',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Option A', 'Option A'), ('Option B', 'Option B'), ('Option C', 'Option C')], max_length=26),
        ),
    ]
