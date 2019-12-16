import json
from unittest import TestCase

from tests.test_base import test_app


class TestBase(TestCase):
    def test_base(self):
        with test_app.test_client() as client:
            rv = client.get("/test")
            self.assertEqual(rv.data.decode(), 'func_test')

    def test_f(self):
        with test_app.test_client() as client:
            rv = client.post("/f", json={'c': 0})
            rv = json.loads(rv.data.decode())
            self.assertFalse(rv['c'])
            rv = client.post("/f", json={'c': 1})
            rv = json.loads(rv.data.decode())
            self.assertTrue(rv['c'])
            rv = client.post("/f", json={'c': 'True'})
            rv = json.loads(rv.data.decode())
            self.assertTrue(rv['c'])
            rv = client.post("/f", json={'c': 'False'})
            rv = json.loads(rv.data.decode())
            self.assertFalse(rv['c'])
            rv = client.post("/f", json={'c': True})
            rv = json.loads(rv.data.decode())
            self.assertTrue(rv['c'])
            rv = client.post("/f", json={'c': False})
            rv = json.loads(rv.data.decode())
            self.assertFalse(rv['c'])

