from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')
        if not full_name:
            raise ValueError('Users must have fullname')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email,full_name, password):

        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email,full_name, password):
        user = self.create_user(
            email,
            full_name,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email       = models.EmailField(
                    verbose_name='email address',
                    max_length=255,
                    unique=True,
                )
    full_name   = models.CharField(max_length=225)
    is_active   = models.BooleanField(default=True)
    staff       = models.BooleanField(default=False)
    admin       = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    objects = UserManager()

class Profile(models.Model):
    user        = models.OneToOneField
