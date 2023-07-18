from django.db import models



'''''
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser

def AppUserManager(AbstractBaseUser):
    phone_number = models.IntegerField(max_length=11)
    text_area = models.CharField(max_length=2000)
    REQUIRED_FIELDS = ["text_area"]

    def __str__(self):
        return self.username

    






from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    number= models.CharField(max_length=11)
    textarea= models.CharField(max_length=2000)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwarks):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwarks):
    instance.profile.save()
'''

