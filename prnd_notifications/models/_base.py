from django.db import models


class BaseNotificationManager(models.Manager):

    class Meta:
        abstract = True


class AbstractBaseNotification(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
