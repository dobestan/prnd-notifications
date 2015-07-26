from django.conf import settings

from prnd_notifications.models.sms import SmsNotification
from ._base import BaseNotificationTask


class SmsNotificationTask(BaseNotificationTask):
    """ Implementation of async SMS notification task.

    References:
        - `API STORE - SMS API Documentation`_

    .. _API STORE - SMS API Documentation:
        http://www.apistore.co.kr/api/apiView.do?service_seq=151
    """

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
