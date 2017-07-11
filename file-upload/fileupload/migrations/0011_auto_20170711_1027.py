# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0010_auto_20170711_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='ekfile',
            name='file_type',
            field=models.CharField(blank=True, default=b'N/A', max_length=10),
        ),
        migrations.AddField(
            model_name='ekfile',
            name='link',
            field=models.CharField(blank=True, default=b'NULL', max_length=500),
        ),
        migrations.AlterField(
            model_name='ekfile',
            name='file',
            field=models.FileField(upload_to=b'../../../var/www/ekstep'),
        ),
    ]
