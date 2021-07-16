'''
contains setup functions called fixtures that each test will use

Pytest uses fixtures by matching their function names 
with the names of arguments in the test functions. 
For example, the test_hello function you will write next takes a client argument. 
Pytest matches that with the client fixture function, 
calls it, and passes the returned value to the test function.
'''

import os
import tempfile
import pytest
from flaskr import create_app
from flaskr.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__),'data.sql'),'rb') as f:
    _data_sql = f.read().decode('utf8')

@pytest.fixture
def app():
    # creates and opens a temporary file, 
    # returning the file descriptor and the path to it.
    db_fd, db_path = tempfile.mkstemp()
    print("tempfile.mkstemp: ",db_fd,db_path)
    app = create_app({
        'TESTING':True,
        'DATABASE':db_path,
    })

    with app.app_context():
        init_db()
        get_db().executescript(_data_sql)
    
    yield app

    os.close(db_fd)
    os.unlink(db_path)

@pytest.fixture
def client(app):
    # The client fixture calls app.test_client() 
    # with the application object created by the app fixture. 
    # Tests will use the client to make requests to the application 
    # without running the server.
    return app.test_client()

@pytest.fixture
def runner(app):
    # The runner fixture is similar to client. 
    # app.test_cli_runner() creates a runner 
    # that can call the Click commands registered with the application.
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data = {'username':username, 'password':password}
        )

    def logout(self):
        return self._client.get('/auth/logout')

# With the auth fixture, 
# you can call auth.login() in a test to log in as the test user,
# which was inserted as part of the test data in the app fixture.
@pytest.fixture
def auth(client):
    return AuthActions(client)