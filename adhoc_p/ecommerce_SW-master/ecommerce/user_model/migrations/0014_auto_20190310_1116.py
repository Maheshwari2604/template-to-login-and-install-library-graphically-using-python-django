# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-10 05:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0013_add_student_fee_paid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_student',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='add_student',
            name='last_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
