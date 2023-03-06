# encoding: utf8

from rest_framework import generics
from rest_framework.response import Response

class DemoView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        resp_data = {
            "code": 200,
            "message": "success"
        }
        return Response(resp_data)
    
    def post(self, request, *args, **kwargs):
        resp_data = {
            "code": 200,
            "message": "success"
        }
        return Response(resp_data)
