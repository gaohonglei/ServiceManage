# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=20)),
                ('registed_date', models.DateTimeField(verbose_name='date registed')),
                ('service_ip', models.CharField(max_length=20)),
                ('service_port', models.IntegerField()),
                ('proxy_string', models.CharField(max_length=100)),
            ],
        ),
    ]
