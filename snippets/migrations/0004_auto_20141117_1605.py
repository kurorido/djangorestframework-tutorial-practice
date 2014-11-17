# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20141117_1602'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ('created',)},
        ),
        migrations.AddField(
            model_name='snippet',
            name='highlighted',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
