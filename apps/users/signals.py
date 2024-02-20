from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.users.models import User


@receiver(post_save, sender=User)
def send_email_user(sender, instance, created, **kwargs):
    send_mail(
        "Welcome",
        "Welcome to goodreads clone",
        "akhmadjonovr.98@gmail.com",
        [instance.email]

    )
