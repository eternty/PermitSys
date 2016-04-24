# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 20:03
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPermitSysApplication', '0005_auto_20160424_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='passport_number',
            field=models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.", regex='^\\{6}$')]),
        ),
        migrations.AlterField(
            model_name='person',
            name='passport_serial',
            field=models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.", regex='^\\{4}$')]),
        ),
    ]
