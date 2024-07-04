from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from a_users.models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        print(f"A user was created {instance}")
        Profile.objects.create(
            user=user,
            email= user.email
        )