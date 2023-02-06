from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import date, datetime
from django.contrib.auth.models import User
from account.models import *
from message.models import RecentActivityModel


@receiver(post_save, sender=User)
def user(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        profile.save()

        wallet = UserWallet.objects.create(user=instance, balance=0)
        wallet.save()


@receiver(post_save, sender=User)
def create_registration_notification(sender, instance, created, **kwargs):

    if created:
        category = 'user_registration'
        subject = instance.username + ' just signed up.'

        activity = RecentActivityModel.objects.create(category=category, subject=subject,
                                                      reference_id=instance.id)
        activity.save()









