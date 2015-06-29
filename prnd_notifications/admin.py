from django.contrib import admin

from prnd_notifications.models import EmailNotification, SlackNotification, SmsNotification


class AbstractBaseNotificationAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', )
    list_display = admin.ModelAdmin.list_display + (
        'created_at',
    )


@admin.register(EmailNotification)
class EmailNotificationAdmin(AbstractBaseNotificationAdmin):
    pass


@admin.register(SlackNotification)
class SlackNotificationAdmin(AbstractBaseNotificationAdmin):
    pass


@admin.register(SmsNotification)
class SmsNotificationAdmin(AbstractBaseNotificationAdmin):
    pass
