from django.db import models

from ._base import BaseNotificationManager, AbstractBaseNotification


class SlackNotificationManager(BaseNotificationManager):
    pass


class SlackNotification(AbstractBaseNotification):
    objects = SlackNotificationManager()
