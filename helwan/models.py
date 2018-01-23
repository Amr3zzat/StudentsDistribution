from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class student(models.Model):

    Computers = 1
    Communications = 2
    Dep_CHOICES = (
        (Computers, 'Computers'),
        (Communications, 'Communications'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dep = models.PositiveSmallIntegerField(choices=Dep_CHOICES, null=True, blank=True)
    deg = models.FloatField(null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

