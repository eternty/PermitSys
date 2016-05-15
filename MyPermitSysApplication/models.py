from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from RequestSysApplication.models import Position, Department

class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    passport_serial_regex = RegexValidator(regex=r'^\d{4}$',
                                               message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.")
    passport_number_regex = RegexValidator(regex=r'^\d{6}$',
                                               message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.")

    passport_serial = models.IntegerField(validators=[passport_serial_regex], blank=True)
    passport_number = models.IntegerField(validators=[passport_number_regex], blank=True)
    #passport_serial = models.IntegerField(blank=True)
    #passport_number = models.IntegerField(blank=True)
    position = models.ForeignKey(Position, verbose_name="Должность", null=True, blank=True)
    department = models.ForeignKey(Department, verbose_name="Отдел")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,
                                    null=True)  # validators should be a list

    class Meta:
        verbose_name = u'Персона'
        verbose_name_plural = u'Персоны'

    is_active = models.BooleanField(default=False)

    def __unicode__(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.patronymic)
        return full_name.strip()


class Permit(models.Model):
    def __unicode__(self):
        return self.name

    #class Meta:
        verbose_name = u'Пропуск'
        verbose_name_plural = u'Пропуска'

    person = models.ForeignKey(Person, related_name="Персона")
    begin_date = models.DateField(auto_now_add=True, verbose_name="Дата создания пропуска")
    end_date = models.DateField(verbose_name="Срок действия пропуска", default='2016-08-30')
    is_active = models.BooleanField(default=True)
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    position = models.ForeignKey(Position, verbose_name="Должность", null=True, blank=True)
    department = models.ForeignKey(Department, verbose_name="Отдел", blank=True, null= True)
    NEW = 'NEW'
    PRINTED = 'PRI'
    PERSON = 'PER'
    LOST = 'LOS'
    OLD = 'OLD'

    PERMIT_STATUSES = (
        (NEW, 'Новый'),
        (PRINTED, 'Напечатан'),
        (PERSON, 'Выдан'),
        (LOST, 'Утерян'),
        (OLD, 'Просрочен')
    )
    status = models.CharField(max_length=3,
                              choices=PERMIT_STATUSES,
                              default=NEW)

    CONTINUOUS = 'CON'
    TEMPORARY = 'TEM'

    PERMIT_TYPES = (
        (CONTINUOUS, 'Постоянный'),
        (TEMPORARY, 'Временный')
    )
    type = models.CharField(max_length=3,
                            choices=PERMIT_TYPES,
                            default=CONTINUOUS)
