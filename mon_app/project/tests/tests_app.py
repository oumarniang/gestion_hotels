import pytest 
from project import main

def index():
    response = main.test_client().get('/')
    assert response.status_code == 200

def bienvenue():
    response = main.test_client().get('/')
    assert response.status_code == 200

def reservations():
    response = main.test_client().get('/')
    assert response.status_code == 200
    assert isinstance(result_data_list, list) == True

def predictions():
    response = main.test_client().get('/')
    assert response.status_code == 200

# def __repr__():
#     # test function __repr__
#     param = 'Oumar'
#     res = __repr__(param)
#     assert isinstance(res, str) == True