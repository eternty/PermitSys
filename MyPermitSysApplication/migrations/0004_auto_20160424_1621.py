# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RequestSysApplication', '0002_auto_20160424_1614'),
        ('MyPermitSysApplication', '0003_auto_20160424_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='position_in_department',
        ),
        migrations.AddField(
            model_name='person',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RequestSysApplication.Department', verbose_name='Отдел'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RequestSysApplication.Position', verbose_name='Должность'),
        ),
    ]
