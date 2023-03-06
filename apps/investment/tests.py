# encoding: utf8

import json
import logging
import unittest
from rest_framework.test import APIClient
from rest_framework.response import Response


class TestInvestment(unittest.TestCase):

    def setUp(self) -> None:
        import django
        django.setup()
        self.client = APIClient()
        self.logger = logging.getLogger("app")

    def test_demo(self):
        resp: Response = self.client.get("/api/v1/demo",)
        assert resp.status_code == 200
        assert resp.data["code"] == 200

        resp: Response = self.client.post("/api/v1/demo", data={}, format="json")
        assert resp.status_code == 200
        assert resp.data["code"] == 200
