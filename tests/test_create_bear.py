import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody


def get_bear_types():
    return [BearBody.BearTypes.BLACK,
            BearBody.BearTypes.BROWN,
            BearBody.BearTypes.GUMMY,
            BearBody.BearTypes.POLAR]


def get_additional_parameters():
    return [("testPar", "test"),
            ("testParInt", 1),
            ("testParDouble", 1.2)]

# Тест на создание медведей по типу
@pytest.mark.parametrize('b_type', get_bear_types())
def test_create_bears_by_type(b_type):
    # Создание медведя
    b_body = BearBody.create_bear_body(b_type, "test", 15.2)
    b_body_json = json.loads(b_body)
    # Запрос на создание медведя
    request = PreparedRequests().createBear(b_body)
    response_post = Session().send(request)
    assert response_post.status_code == 200

    bear_id = int(response_post.text)
    # Запрос на получение медведя
    request = PreparedRequests().getSpecificBear(bear_id)
    response_get = Session().send(request)
    # Проверка медведя
    assert response_get.status_code == 200
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper()
    assert response_get.json()["bear_id"] == bear_id
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper()
    assert response_get.json()["bear_age"] == b_body_json["bear_age"]

# Тест на создание медведей c дополниельными полями в запросе
@pytest.mark.parametrize('add_par, add_val', get_additional_parameters())
def test_create_bears_with_additional_parameters(add_par, add_val):
    # Создание медведя
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2, add_par, add_val)
    b_body_json = json.loads(b_body)
    # Запрос на создание медведя
    request = PreparedRequests().createBear(b_body)
    response_post = Session().send(request)
    assert response_post.status_code == 200

    bear_id = int(response_post.text)
    # Запрос на получение медведя
    request = PreparedRequests().getSpecificBear(bear_id)
    response_get = Session().send(request)
    # Проверка медведя
    assert response_get.status_code == 200
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper()
    assert response_get.json()["bear_id"] == bear_id
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper()
    assert response_get.json()["bear_age"] == b_body_json["bear_age"]
    assert add_par not in response_get.json()
