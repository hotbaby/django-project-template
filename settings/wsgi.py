"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.signals import got_request_exception
from django.dispatch import receiver

os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                      os.environ.get("DJANGO_SETTINGS_MODULE", "settings.staging"))


def check():
    import json
    from django.conf import settings
    from apps.utils.sql import sql_query
    from apps.utils.redis_ import redis_cli

    print(f"DJANGO_SETTINGS_MODULE: {os.environ.get('DJANGO_SETTINGS_MODULE')}")

    mysql_host = settings.DATABASES["default"]["HOST"]
    print(f"Check database connection, mysql_host: {mysql_host}")
    sql_query("select now() time_now")
    print(f"Check database connection successfully")

    print(f"Check redis connection, redis_host: {settings.REDIS_HOST}")
    redis_cli.time()
    print("Check redis connection successfully")


check()


@receiver(got_request_exception)
def debug_django_exception(**kwargs):
    import sys
    import logging
    from django.conf import settings

    logger = logging.getLogger("app")
    traceback = sys.exc_info()[2]
    logger.exception(traceback)


application = get_wsgi_application()
