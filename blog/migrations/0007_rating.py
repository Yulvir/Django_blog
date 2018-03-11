# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180304_1746'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ratings', multiselectfield.db.fields.MultiSelectField(max_length=200, verbose_name=(('Option A',), ('Option B',), ('Option C',)))),
                ('post', models.ForeignKey(related_name='rating', to='blog.Post')),
            ],
        ),
    ]
