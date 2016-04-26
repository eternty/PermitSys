# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-23 21:19
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
            },
        ),
        migrations.CreateModel(
            name='Permit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_date', models.DateField(auto_now_add=True, verbose_name='Дата создания пропуска')),
                ('end_date', models.DateField(verbose_name='Срок действия пропуска')),
                ('is_active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('NEW', 'Новый'), ('PRI', 'Напечатан'), ('PER', 'Выдан'), ('LOS', 'Утерян'), ('OLD', 'Просрочен')], default='NEW', max_length=3)),
                ('type', models.CharField(choices=[('CON', 'Постоянный'), ('TEM', 'Временный')], default='CON', max_length=3)),
            ],
            options={
                'verbose_name': 'Пропуск',
                'verbose_name_plural': 'Пропуска',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('passport_serial', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.", regex='^\\?1?\\d{4}$')])),
                ('passport_number', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.", regex='^\\?1?\\d{4}$')])),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Персоны',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
            },
        ),
        migrations.CreateModel(
            name='PositionInDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyPermitSysApplication.Department')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyPermitSysApplication.Position')),
            ],
            options={
                'verbose_name': 'Специализация',
                'verbose_name_plural': 'Специализации',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('patronymic', models.CharField(max_length=20)),
                ('passport_serial', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.", regex='^\\?1?\\d{4}$')])),
                ('passport_number', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.", regex='^\\?1?\\d{4}$')])),
                ('registration_date', models.DateField(auto_now_add=True, verbose_name='Дата создания заявки')),
                ('end_date', models.DateField(verbose_name='Срок действия пропуска')),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('NEW', 'Новая'), ('APR', 'Утверждена'), ('CAN', 'Отменена'), ('DON', 'Выполнена')], default='NEW', max_length=3)),
                ('position_in_department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyPermitSysApplication.PositionInDepartment', verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.AddField(
            model_name='person',
            name='position_in_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MyPermitSysApplication.PositionInDepartment', verbose_name='Должность'),
        ),
        migrations.AddField(
            model_name='permit',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Персона', to='MyPermitSysApplication.Person'),
        ),
    ]