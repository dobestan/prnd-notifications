from prnd_notifications.models.slack import SlackNotification
from ._base import BaseNotificationTask

import json


class SlackNotificationTask(BaseNotificationTask):
    """ Implementation of async Slack notification task.

    References:
        - `Slack Incoming Webhooks API Documentation`_

    .. _Slack Incoming Webhooks API Documentation:
        https://api.slack.com/incoming-webhooks
    """
    model = SlackNotification
    base_url = "https://hooks.slack.com/services/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"

    def _get_notification_payload(self, instance):
        payload = {
            "username": instance.sender,
            "channel": instance.receiver,
            "text": instance.content,
        }

        return json.dumps(payload)
