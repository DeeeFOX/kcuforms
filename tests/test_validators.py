from unittest import TestCase

from kcuforms.validators import list_type


class ValidatorTest(TestCase):

    def test01_index(self):
        self.assertEqual(list_type('["1", "2"]'), ["1", "2"])
