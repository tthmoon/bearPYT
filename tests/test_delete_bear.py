import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody

# Фикстура для создания медведя, передает в тест id медведя
@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)

    request = PreparedRequests().createBear(b_body)
    response_post = Session().send(request)
    assert response_post.status_code == 200

    bear_id = int(response_post.text)

    return bear_id

# Тест на удаление определенного медведя
def test_delete_specific_bear(prepare_and_create_bear):
    # Запрос на удаление медведя
    request = PreparedRequests().deleteSpecificBear(prepare_and_create_bear)
    response_delete = Session().send(request)
    assert response_delete.status_code == 200
    assert response_delete.text == "OK"
    # Запрос за получение медведя
    request = PreparedRequests().getSpecificBear(prepare_and_create_bear)
    response_get = Session().send(request)
    assert response_get.status_code == 200
    assert response_get.text == "EMPTY"

# Тест на удаление всех медведей
def test_delete_all_bear(prepare_and_create_bear):
    # Запроса на удаление всех медведей
    request = PreparedRequests().deleteAllBear()
    response_delete = Session().send(request)
    assert response_delete.status_code == 200
    assert response_delete.text == "OK"
    # Запрос на получение всех медведей
    request = PreparedRequests().getAllBears()
    response_get = Session().send(request)
    bears = json.loads(response_get.text)
    # Проверка, что список медведй пустой
    assert len(bears) == 0
