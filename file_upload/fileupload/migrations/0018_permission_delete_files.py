# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0017_auto_20170717_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='delete_files',
            field=models.BooleanField(default=False),
        ),
    ]
