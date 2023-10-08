from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"))
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password", "fullname"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
