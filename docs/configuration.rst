=============
Configuration
=============


Basic Configuration
-------------------

`prnd_notifications`_ 어플리케이션은 Django Admin Integration 을 지원합니다. Django Admin 에서 알림내역이나 전송 여부를 확인하기 위해서는 ``INSTALLED_APP`` 에 ``prnd_notifications`` 을 추가하면 됩니다:

::

    INSTALLED_APPS = (
        'django.contrib.auth',
        ...
        'prnd_notifications',
        ...
    )
    


Database Migration
------------------

::

    $ manage.py makemigrations [prnd_notifications]
    $ manage.py migrate


Celery Integration
------------------

`prnd_notifications`_ 은 개발자 및 서비스 이용자에게 빠른 반응성을 보장하기 위해서 모든 Notification API ( SMS, Email, Slack ) 호출에 Async Task 를 사용하고 있습니다. 따라서, 개발 환경이나 배포 환경에서 Celery 프로세스를 띄워둔 상태에서만 정상적으로 알림을 보낼 수 있습니다.

::

    $ celery --workdir=[WORK_DIR] --app=[APP_NAME].celery:app --concurrency=[NUM_OF_WORKERS] worker


PRND Company 의 모든 어플리케이션은 Procfile Based Application 이므로 아래의 명령어로도 Celery Process를 실행시킬 수 있습니다:

::

    $ honcho start worker

.. _`prnd_notifications`: https://github.com/PRNDcompany/prnd-notifications
