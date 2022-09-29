from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import timedelta

from analytics.models import CapturedData, UniqueVisitor

print('django signal loaded!')


@receiver(post_save, sender=CapturedData)
def validate_data_and_create_unique_visitors(sender: CapturedData, instance: CapturedData, *args, **kwargs):
    history = CapturedData.objects.filter(s3=instance.s3, ip_address=instance.ip_address)

    if history.count() > 1:
        latest = history.order_by('-created_at')[1]

        if latest.created_at + timedelta(minutes=30) < instance.created_at:
            UniqueVisitor(data=instance).save()
    else:
        UniqueVisitor(data=instance).save()
