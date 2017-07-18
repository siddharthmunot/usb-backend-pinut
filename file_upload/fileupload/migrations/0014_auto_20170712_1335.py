# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-12 11:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0013_auto_20170711_1056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_file', models.CharField(max_length=250)),
                ('json_file', models.CharField(max_length=250)),
            ],
        ),
        migrations.RemoveField(
            model_name='ekfile',
            name='file_type',
        ),
        migrations.RemoveField(
            model_name='ekfile',
            name='link',
        ),
        migrations.AddField(
            model_name='ekfile',
            name='path_of_file',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='ekfile',
            name='type_of_file',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='content',
            name='ekfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fileupload.EkFile'),
        ),
    ]
