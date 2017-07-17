# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 05:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fileupload', '0014_auto_20170712_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('down_to_usb', models.BooleanField(default=False)),
                ('up_from_usb', models.BooleanField(default=False)),
                ('up_from_dev', models.BooleanField(default=False)),
                ('ssid_mod', models.BooleanField(default=False)),
                ('captive_mod', models.BooleanField(default=False)),
                ('global_vars_mod', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
