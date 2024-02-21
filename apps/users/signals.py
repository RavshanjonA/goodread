from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User
from apps.users.tasks import send_email


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    if created:
        send_email.delay("Welcome to goodreads site", "We are happy to see you here", [instance.email])
