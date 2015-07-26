from django.db import models
from django.db.models.signals import post_save

from ._base import BaseNotificationManager, AbstractBaseNotification


class SlackNotificationManager(BaseNotificationManager):
    pass


class SlackNotification(AbstractBaseNotification):
    objects = SlackNotificationManager()


def post_save_slack_notification(sender, instance, created, **kwrags):
    from prnd_notifications.tasks import SlackNotificationTask

    if created:
        if not instance.sender:
            instance.sender = "prnd_notifications"
            instance.save()

        if not instance.receiver:
            instance.receiver = "develop"
            instance.save()

        task = SlackNotificationTask()
        task.delay(instance.id)

post_save.connect(post_save_slack_notification, sender=SlackNotification)


def send_slack(*args, **kwargs):
    return SlackNotification.objects.create(*args, **kwargs)
