# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-03-08 05:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_model', '0010_add_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_student',
            name='Cource_fee',
            field=models.PositiveIntegerField(help_text='Required'),
        ),
        migrations.AlterField(
            model_name='add_student',
            name='father_contact_no',
            field=models.PositiveIntegerField(help_text='Required'),
        ),
    ]
