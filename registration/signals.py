from django.db.models.signals import post_save, pre_delete
from .models import User,Profile
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('signal test created')
        Profile.objects.create(user=instance)
    else:
        print('signal test not created')