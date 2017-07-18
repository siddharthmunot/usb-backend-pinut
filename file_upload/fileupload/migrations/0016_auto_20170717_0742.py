# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 05:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0015_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
