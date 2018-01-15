from django.contrib.auth.models import User
from django.db import models
from django.db.models.functions import datetime
from django.urls import reverse

TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)
    last_accessed = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)


class Writer(models.Model):
    name = models.CharField(max_length=100)


class Publish(models.Model):
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=100)

class Student(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # used with UpdateView and CreateView as a redirect url after filling the form
    def get_absolute_url(self):
        # return reverse('student-detail', kwargs={'pk': self.pk})
        return reverse('morepractice:thanks')



