# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0002_remove_gzyservice_service_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='gzyservice',
            name='service_id',
            field=models.CharField(default='abc', max_length=20),
        ),
    ]