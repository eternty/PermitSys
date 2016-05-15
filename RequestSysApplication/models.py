from django.utils import timezone
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class Department(models.Model):
    name = models.CharField(verbose_name= u'Тип', max_length=30, null=True, blank = True)
    number = models.CharField(verbose_name= u'Имя',max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,
                                    null=True)  # validators should be a list
    info = models.CharField(max_length=200, blank=True, null=True)
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
    #class Meta:
     #   verbose_name = u'Заявка'
      #  verbose_name_plural = u'Заявки'
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
    #phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
     #                            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    #phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True,
    #                                null=True)  # validators should be a list
    phone_number = models.CharField(max_length=15,  blank=True,
                                    null=True)  # validators should be a list
    department = models.ForeignKey(Department, verbose_name="Отдел", null=True)
    position = models.ForeignKey(Position, verbose_name="Должность", null=True)

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

"""class MyUserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password,
                                 True, True, **extra_fields)

class User_type(models.Model):
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'Тип пользователя'
        verbose_name_plural = u'Типы пользователей'

    name = models.CharField(max_length=20)
    info = models.CharField(max_length=100)


class System_User(AbstractBaseUser, PermissionsMixin):
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def get_full_name(self):
        full_name = '%s %s %s' % (self.first_name, self.patronymic, self.last_name)
        return full_name.strip()

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
        ordering = ('-date_joined', )

    email = models.EmailField(_('email address'), max_length=100, unique=True)
    username = models.CharField(_('username'), max_length=50, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    usertype = models.ForeignKey(User_type, null=True)

    def __unicode__(self):
        return self.username
"""
