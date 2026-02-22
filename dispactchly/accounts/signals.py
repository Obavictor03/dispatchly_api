from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rider, Sender, User

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'seller':
            Sender.objects.create(user=instance)
        elif instance.role == 'rider':
            Rider.objects.create(user=instance)