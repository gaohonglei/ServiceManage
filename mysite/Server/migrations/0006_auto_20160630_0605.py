# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-30 06:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0005_auto_20160629_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gzymediaservice',
            old_name='MaxDeviceCount',
            new_name='MaxClientCount',
        ),
    ]