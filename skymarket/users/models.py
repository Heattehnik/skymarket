from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoleEnum(models.TextChoices):
    USER = "user"
    ADMIN = "admin"


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    role = models.CharField(max_length=10, choices=UserRoleEnum.choices, default=UserRoleEnum.USER)
    avatar = models.ImageField(upload_to='django_media/avatars', default='avatars/default.png',
                               verbose_name="Аватар", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoleEnum.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoleEnum.USER

