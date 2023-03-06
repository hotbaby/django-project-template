# encoding: utf8

from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": 3306,
        "OPTIONS": {
            "charset": "utf8mb4",
            "use_unicode": True,
        },
    }
}

# Redis Configuration
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = ""


# OSS Configuration
OSS_ACCESS_KEY_ID = "TODO OSS账号"
OSS_ACCESS_SECRET_ID = "TODO OSS密码"
OSS_ENDPOINT = "TODO OSS Endpoint"   # 例如：oss-cn-beijing.aliyuncs.com
OSS_BUCKET_NAME = "TODO OSS Bucket名字"