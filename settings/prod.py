# encoding: utf8

from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "TODO MySQL数据库名称",
        "USER": "TODO MySQL账号",
        "PASSWORD": "TODO MySQL密码",
        "HOST": "TODO MySQL Host",
        "PORT": 3306,
        "OPTIONS": {
            "charset": "utf8mb4",
            "use_unicode": True,
        },
    }
}

# Redis Configuration
REDIS_HOST = "TODO Redis Host"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PASSWORD = "TODO Redis密码"


# OSS Configuration
OSS_ACCESS_KEY_ID = "TODO OSS账号"
OSS_ACCESS_SECRET_ID = "TODO OSS密码"
OSS_ENDPOINT = "TODO OSS Endpoint"   # 例如：oss-cn-beijing.aliyuncs.com
OSS_BUCKET_NAME = "TODO OSS Bucket名字"