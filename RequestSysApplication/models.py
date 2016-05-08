from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,
                                    null=True)  # validators should be a list

    class Meta:
        verbose_name = u'Отдел'
        verbose_name_plural = u'Отделы'

    def __str__(self):
        full_name = '%s %s' % (self.name, self.number)
        return full_name.strip()

    def get_name(self):
        full_name = '%s %s' % (self.name, self.number)
        return full_name.strip()

    def __unicode__(self):
        full_name = '%s %s' % (self.name, self.number)
        return full_name.strip()

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


class MyRequest(models.Model):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    patronymic = models.CharField(max_length=20, blank=True, null=True)
    # passport_serial_regex = RegexValidator(regex=r'^\?1?\d{0,4}$',
    # message="Passport Serial must be entered in the format: '9999'. Up to 4 digits allowed.")
    # passport_number_regex = RegexValidator(regex=r'^\?1?\d{0,6}$',
    # message= "Passport Number must be entered in the format: '999999'. Up to 6 digits allowed.")
    # passport_serial = models.IntegerField(validators=[passport_serial_regex], blank=True)
    # passport_number = models.IntegerField(validators=[passport_number_regex], blank=True)

    passport_serial = models.IntegerField(blank=True)
    passport_number = models.IntegerField(blank=True)
    registration_date = models.DateField(auto_now_add=True, verbose_name="Дата создания заявки")
    end_date = models.DateField(verbose_name="Срок действия пропуска", default='2016-08-30')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,
                                    null=True)  # validators should be a list
    department = models.ForeignKey(Department, verbose_name="Отдел", null=True)
    position = models.ForeignKey(Position, verbose_name="Должность", null=True)

    #def creation(lastname, firstname, patronymic, department, position, passport_number, passport_serial, phone_number, end_date):
        #reqobject = Request.objects.create()
        #reqobject = MyRequest.objects.create()
        #reqobject.firstname = firstname
        #reqobject.lastname = lastname
        #reqobject.patronymic = patronymic
        #reqobject.department = department.id
        #reqobject.position = position.id
        #reqobject.end_date = end_date
        #reqobject.passport_serial = passport_serial
        #reqobject.passport_number = passport_number
        #reqobject.phone_number = phone_number
        #return reqobject
    @staticmethod
    def creation(form):
        myrequest = form.save()
        return myrequest

    @staticmethod
    def deletion(req_id):
        MyRequest.objects.get(id=req_id).delete()

        return 0

    def request_proceed(self,choice):
        if choice == u'approve':
            self.status = u'APR'
        if choice == u'decline':
            self.status = u'DEC'
        self.save()
        return self

    def update_info(self,our_form):

        self.firstname = our_form.cleaned_data['firstname']
        self.lastname = our_form.cleaned_data['lastname']
        self.patronymic = our_form.cleaned_data['patronymic']
        self.department = our_form.cleaned_data['department']
        self.position = our_form.cleaned_data['position']
        self.end_date = our_form.cleaned_data['end_date']
        self.passport_number = our_form.cleaned_data['passport_number']
        self.passport_serial = our_form.cleaned_data['passport_serial']
        self.phone_number = our_form.cleaned_data['phone_number']
        self.status = our_form.cleaned_data['status']
        self.save()
        return self


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


