

from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser,BaseUserManager

from django.conf import settings


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Вниз'),
        ('medium', 'В среднем'),
        ('high', 'Вверх'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    description = models.TextField(blank=True, null=True, verbose_name="Подробнее")
    due_date = models.DateTimeField(blank=True, null=True, verbose_name="Срок исполнения")
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium', verbose_name="Важность")
    is_completed = models.BooleanField(default=False, verbose_name="Сделанный")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.title


class CustomUserManager(BaseUserManager):
    def create_user(self, login, email, password=None, **extra_fields):
        if not login:
            raise ValueError('Логин должно быть написано!')
        if not email:
            raise ValueError('Email должно быть написано!')

        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(login, email, password, **extra_fields)



class CustomUser(AbstractUser):
    login = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    username = None

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

    def __str__(self):
        return self.login
