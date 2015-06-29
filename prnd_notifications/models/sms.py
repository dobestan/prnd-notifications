from django.db import models

from ._base import BaseNotificationManager, AbstractBaseNotification


class SmsNotificationManager(BaseNotificationManager):
    pass


class SmsNotification(AbstractBaseNotification):
    objects = SmsNotificationManager()
