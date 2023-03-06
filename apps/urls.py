"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""

import logging
from django.conf.urls import include, url
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import generics
from rest_framework.request import Request
from rest_framework.response import Response
from django.http.response import JsonResponse

logger = logging.getLogger("app")


schema_view = get_schema_view(
    openapi.Info(
        title="API接口文档",
        default_version="v1",
        description="API接口文档",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


class HealthView(generics.GenericAPIView):

    def get(self, request: Request, *args, **kwargs) -> Response:
        resp_data = {
            "code": 200,
            "message": "success",
            "data": {
                "status": "alive"
            }
        }
        return JsonResponse(resp_data)


urlpatterns = [
    url("^api/v1/", include("apps.investment.urls")),
    re_path("^api/v1/health$", HealthView.as_view(), name="health"),
    path("swagger", schema_view.with_ui("swagger", cache_timeout=0)),
] + staticfiles_urlpatterns()


def bad_request(request, exception, *args, **kwargs):
    data = {
        "code": 400,
        "message": "Bad Request"
    }
    return JsonResponse(data, status=400)


def permission_denied(request, exception, *args, **kwargs):
    data = {
        "code": 403,
        "message": "Forbidden"
    }

    return JsonResponse(data, status=403)


def page_not_found(request, exception, *args, **kwargs):
    data = {
        "code": 404,
        "message": "Not Found"
    }
    return JsonResponse(data, status=404)


def server_error(*args, **kwargs):
    data = {
        "code": 500,
        "message": "Server Error"
    }
    return Response(data, status=500)


handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = server_error
