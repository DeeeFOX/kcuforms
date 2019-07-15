from unittest import TestCase

from kcuforms.form import WebForm
from kcuforms.fields import IntegerField


class IntegerFieldTest(TestCase):
    class F(WebForm):
        a = IntegerField(default=10)
        b = IntegerField(default=48)

    def test(self):
        self.assertEqual(self.F().get_form(), {'a': 10, 'b': 48})
