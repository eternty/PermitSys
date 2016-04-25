from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True)  # validators should be a list
    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'
    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = u'Должность'
        verbose_name_plural = u'Должности'
    info = models.CharField(max_length=200, blank=True, null=True)

    def get_name(self):
        return self.name

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class Request(models.Model):

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    #passport_serial_regex = RegexValidator(regex=r'^\?1?\d{0,4}$',
                                           #message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.")
    #passport_number_regex = RegexValidator(regex=r'^\?1?\d{0,6}$',
                                       #message= "Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.")
    #passport_serial = models.IntegerField(validators=[passport_serial_regex], blank=True)
    #passport_number = models.IntegerField(validators=[passport_number_regex], blank=True)

    passport_serial = models.IntegerField(blank=True, null=True)
    passport_number = models.IntegerField(blank=True, null=True)
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата создания заявки")
    end_date = models.DateField(verbose_name="Срок действия пропуска")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,null=True)  # validators should be a list
    department = models.ForeignKey(Department, verbose_name= "Отдел",null=True)
    position = models.ForeignKey(Position, verbose_name="Должность", null=True)

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


