from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoleEnum(models.TextChoices):
    USER = "USER"
    ADMIN = "ADMIN"


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name="Электронная почта", unique=True)
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    role = models.CharField(max_length=10, choices=UserRoleEnum.choices)
    avatar = models.ImageField(verbose_name="Аватар")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    objects = UserManager()

    @property
    def is_admin(self):
        return self.role == UserRoleEnum.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoleEnum.USER

