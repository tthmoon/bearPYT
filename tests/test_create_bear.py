import json

import pytest
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
    response_post = PreparedRequests().createBear(b_body)

    assert response_post.status_code == 200, "Response status code does not match expected"

    bear_id = int(response_post.text)
    # Запрос на получение медведя
    response_get = PreparedRequests().getSpecificBear(bear_id)
    # Проверка медведя
    assert response_get.status_code == 200, "Response status code does not match expected"
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper(),\
        "Created bear type does not match expected"
    assert response_get.json()["bear_id"] == bear_id, \
        "Created bear id does not match expected"
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper(), \
        "Created bear name does not match expected"
    assert response_get.json()["bear_age"] == b_body_json["bear_age"], "Created bear age does not match expected"


# Тест на создание медведей c дополниельными полями в запросе
@pytest.mark.parametrize('add_par, add_val', get_additional_parameters())
def test_create_bears_with_additional_parameters(add_par, add_val):
    # Создание медведя
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2, add_par, add_val)
    b_body_json = json.loads(b_body)
    # Запрос на создание медведя
    response_post = PreparedRequests().createBear(b_body)

    assert response_post.status_code == 200, "Response status code does not match expected"

    bear_id = int(response_post.text)
    # Запрос на получение медведя
    response_get = PreparedRequests().getSpecificBear(bear_id)
    # Проверка медведя
    assert response_get.status_code == 200, "Response status code does not match expected"
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper(), \
        "Created bear type does not match expected"
    assert response_get.json()["bear_id"] == bear_id, "Created bear id does not match expected"
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper(), \
        "Created bear name does not match expected"
    assert response_get.json()["bear_age"] == b_body_json["bear_age"], "Created bear age does not match expected"
    assert add_par not in response_get.json(), "An extra parameter '{}' was found in the body of a bear".format(add_par)
