from django.db.models.signals import post_delete
from django.dispatch import receiver

from S3.models import S3

print('S3 signal loaded!')


@receiver(post_delete, sender=S3)
def validate_data_and_create_unique_visitors(sender: S3, instance: S3, *args, **kwargs):
    result = instance.security_result
    result.delete()
