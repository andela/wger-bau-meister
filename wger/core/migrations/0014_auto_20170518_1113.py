# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-18 08:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20170518_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apiuser',
            old_name='user_created_by',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='apiuser',
            old_name='username',
            new_name='user',
        ),
    ]
