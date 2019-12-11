from kcuforms import WebForm, IntegerField, BooleanField
from tests.test_base import test_app


class F(WebForm):
    a = IntegerField(default=10)
    b = IntegerField(default=48)
    c = BooleanField(default=True)


@test_app.route('/f', methods=['POST'])
def func_F():
    f = F().get_form()
    return f
