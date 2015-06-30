from celery import Task
import requests


class BaseNotificationTask(Task):
    abstract = True

    def run(self, instance_id):
        instance = self._get_instance(instance_id)
        payload = self._get_notification_payload(instance)
        headers = self._get_notification_headers(instance)

        response = requests.post(
            self.base_url,
            data=payload,
            headers=headers,
        )

        self._update_instance_with_response(instance, response)

        return response

    def _get_instance(self, instance_id):
        return self.model.objects.get(id=instance_id)

    def _get_notification_headers(self, instance):
        headers = {}
        return headers

    def _get_notification_payload(self, instance):
        payload = {}
        return payload

    def _update_instance_with_response(self, instance, response):
        instance.status_code = response.status_code
        instance.response_content = response.content
        instance.save()
