from django.contrib.auth.models import User
from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    author_name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_books')

    # through='UserBookRelation' - означает что для реализации связи ManyToMany используется не дефолтная модель.
    readers = models.ManyToManyField(User, through='UserBookRelation', related_name='books')

    def __str__(self):
        return f'id {self.id}: {self.name}'


class AllUsers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mail = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=20)


class UserBookRelation(models.Model):
    """ Заменяет дефолтную модель которая создается если не указать through='UserBookRelation' """
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Fine'),
        (3, 'Good'),
        (4, 'Amazing'),
        (5, 'Incredible')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f' {self.user.username}: {self.book.name}, RATE: {self.rate}'
