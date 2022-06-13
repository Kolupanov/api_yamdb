# api_yamb/|User/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    '''Добавление поля Биография.'''
    bio = models.TextField(
        'Биография',
        help_text='Тут может быть биография пользователя',
        blank=True,
    )
