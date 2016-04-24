from django.db import models

# Create your models here.

from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

class Department(models.Model):
    name = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'


class Position(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = u'Должность'
        verbose_name_plural = u'Должности'
    info = models.CharField(max_length=200)


class PositionInDepartment(models.Model):
    class Meta:
        verbose_name = u'Специализация'
        verbose_name_plural = u'Специализации'

    position = models.ForeignKey(Position)
    department = models.ForeignKey(Department)

    def get_position_name(self):
        return self.position.name

    def __unicode__(self):
        full_recognition = '%s %s' % (self.position.name, self.department.name)
        return full_recognition.strip()


class Person(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    passport_serial_regex = RegexValidator(regex=r'^\?1?\d{4}$',
                                 message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.")
    passport_number_regex = RegexValidator(regex=r'^\?1?\d{4}$',
                                 message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.")

    passport_serial = models.IntegerField(validators=[passport_serial_regex], blank=True)
    passport_number = models.IntegerField(validators=[passport_number_regex], blank=True)
    position_in_department = models.ForeignKey(PositionInDepartment, verbose_name= "Должность", null=True, blank = True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length= 15, validators=[phone_regex], blank=True)  # validators should be a list
    class Meta:
        verbose_name = u'Персона'
        verbose_name_plural = u'Персоны'

    is_active = models.BooleanField(default=False)


class Request(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20)
    passport_serial_regex = RegexValidator(regex=r'^\?1?\d{4}$',
                                           message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.")
    passport_number_regex = RegexValidator(regex=r'^\?1?\d{4}$',
                                       message="Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.")
    passport_serial = models.IntegerField(validators=[passport_serial_regex], blank=True)
    passport_number = models.IntegerField(validators=[passport_number_regex], blank=True)
    position_in_department = models.ForeignKey(PositionInDepartment, verbose_name="Должность", null=True, blank=True)
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата создания заявки")
    end_date = models.DateField(verbose_name="Срок действия пропуска")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list

    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'


    createtime = models.DateTimeField(default=timezone.now)
    NEW = 'NEW'
    APPROVED = 'APR'
    CANCELLED = 'CAN'
    DONE = 'DON'

    REQUEST_STATUSES = (
        (NEW, 'Новая'),
        (APPROVED, 'Утверждена'),
        (CANCELLED, 'Отменена'),
        (DONE, 'Выполнена'),
    )
    status = models.CharField(max_length=3,
                              choices=REQUEST_STATUSES,
                              default=NEW)


class Permit(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Пропуск'
        verbose_name_plural = u'Пропуска'
    person = models.ForeignKey(Person, related_name="Персона")
    begin_date = models.DateField( auto_now_add=True, verbose_name="Дата создания пропуска")
    end_date = models.DateField(verbose_name="Срок действия пропуска")
    is_active = models.BooleanField(default=True)

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

    PERMIT_TYPES= (
        (CONTINUOUS, 'Постоянный'),
        (TEMPORARY, 'Временный')
    )
    type = models.CharField(max_length=3,
                              choices=PERMIT_TYPES,
                              default=CONTINUOUS)