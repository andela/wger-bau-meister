# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-18 16:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_userprofile_adding_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='adding_permissions',
            field=models.BooleanField(default=False),
        ),
    ]
