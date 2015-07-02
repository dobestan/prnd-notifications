from django.db import models

from ._base import BaseNotificationManager, AbstractBaseNotification


class EmailNotificationManager(BaseNotificationManager):
    pass


class EmailNotification(AbstractBaseNotification):
    objects = EmailNotificationManager()
