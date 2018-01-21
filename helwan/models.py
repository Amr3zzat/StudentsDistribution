from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    STUDENT = 1
    Professor = 2
    Head = 3
    ROLE_CHOICES = (
        (STUDENT, 'STUDENT'),
        (Professor, 'Professor'),
        (Head, 'Head'),
    )
    Computers = 1
    Communications = 2
    Dep_CHOICES = (
        (Computers, 'Computers'),
        (Communications, 'Communications'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dep = models.PositiveSmallIntegerField(choices=Dep_CHOICES, null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()