# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-19 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20170718_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='birthday',
            field=models.DateTimeField(),
        ),
    ]