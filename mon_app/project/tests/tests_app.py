import pytest 
from project import app

def index():
    response = app.test_client().get('/')
    assert response.status_code == 200

def about():
    response = app.test_client().get('/')
    assert response.status_code == 200

def __repr__():
    # test function __repr__
    param = 'Oumar'
    res = __repr__(param)
    assert isinstance(res, str) == True