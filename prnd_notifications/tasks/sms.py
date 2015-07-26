from prnd_notifications.models.sms import SmsNotification
from ._base import BaseNotificationTask

import json


class SmsNotificationTask(BaseNotificationTask):
    model = SmsNotification
    base_url = "http://api.openapi.io/ppurio/1/message/sms/prnd"

    def _get_notification_headers(self, instance):
        headers = {
            "x-waple-authorization": "Mjc4NC0xNDM3MzcyNzk3NzM0LTgzMDA5NjYzLTZkYjQtNGUyYy04MDk2LTYzNmRiNGFlMmMxNw==",
        }

        return headers

    def _get_notification_payload(self, instance):
        payload = {
            "send_phone": instance.sender, 
            "dest_phone": instance.receiver, 
            "msg_body": instance.content, 
        }

        return payload
