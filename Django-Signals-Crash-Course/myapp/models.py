from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    user = ForeignKey(User, on_delete=models.CASCADE)

@receiver(pre_save, sender=User)
def user_pre_created_handler(*args, **kwargs):
    print('User will be created...')

@receiver(post_save, sender=User)
def user_post_created_handler(sender, instance, created, *args, **kwargs):
    if created:
        Profile.objects.create(first_name=instance.first_name, user=instance)

# pre_save.connect(user_pre_created_handler, sender=User)
# post_save.connect(user_post_created_handler, sender=User)

class Audit(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=255, blank=True, null=True)

@receiver(pre_delete, sender=User)
def user_pre_deleted_handler(sender, instance, *args, **kwargs):
    print('User will be deleted...')

@receiver(post_delete, sender=User)
def user_post_deleted_handler(sender, instance, *args, **kwargs):
    Audit.objects.create(username=instance.username)