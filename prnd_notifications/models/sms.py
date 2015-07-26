from django.db import models
from django.db.models.signals import post_save

from ._base import BaseNotificationManager, AbstractBaseNotification


class SmsNotificationManager(BaseNotificationManager):
    pass


class SmsNotification(AbstractBaseNotification):
    objects = SmsNotificationManager()


def post_save_sms_notification(sender, instance, created, **kwrags):
    from prnd_notifications.tasks import SmsNotificationTask

    if created:
        task = SmsNotificationTask()
        task.delay(instance.id)

post_save.connect(post_save_sms_notification, sender=SmsNotification)
