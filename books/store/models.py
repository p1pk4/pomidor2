from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id {self.id}: {self.name}'


class AllUsers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mail = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)
