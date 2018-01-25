from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import ModelForm


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

    def __str__(self):
        return self.user.username


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        student.objects.create(user=instance)


def save_user_profile(sender, instance, **kwargs):
    instance.student.save()



class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class studentForm(ModelForm):
    class Meta:
        model = student
        fields = ('dep', 'deg')
