from django.db import models


class BaseNotificationManager(models.Manager):

    class Meta:
        abstract = True


class AbstractBaseNotification(models.Model):

    sender = models.CharField(max_length=255, blank=True, null=True)
    receiver = models.CharField(max_length=255, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
