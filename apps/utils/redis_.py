# encoding: utf8

from redis import Redis
from django.conf import settings


redis_cli = Redis(host=settings.REDIS_HOST, 
                  port=settings.REDIS_PORT,
                  db=settings.REDIS_DB, 
                  password=settings.REDIS_PASSWORD)

