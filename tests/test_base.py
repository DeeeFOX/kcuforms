from tests import context
import os
import tempfile
import pytest
from flask import Flask

test_app = Flask(__name__)


@test_app.route('/test', methods=['GET'])
def func_test():
    return "func_test"


@pytest.fixture(scope='module')
def client(request):
    db_fd, test_app.config['FSDB_CONFIG'] = tempfile.mkstemp()
    test_client = test_app.test_client()
    with test_app.app_context():
        yield test_client

    os.close(db_fd)
    os.unlink(test_app.config['FSDB_CONFIG'])
