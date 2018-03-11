# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='rate',
        ),
        migrations.AddField(
            model_name='post',
            name='options',
            field=multiselectfield.db.fields.MultiSelectField(max_length=1, choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]
