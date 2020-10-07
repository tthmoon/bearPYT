import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody

# Фикстура для создания медведя, передает в тест id медведя
@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)

    response_post = PreparedRequests().createBear(b_body)

    assert response_post.status_code == 200, "Response status code does not match expected"

    bear_id = int(response_post.text)

    return bear_id

# Тест на удаление определенного медведя
def test_delete_specific_bear(prepare_and_create_bear):
    # Запрос на удаление медведя
    response_delete = PreparedRequests().deleteSpecificBear(prepare_and_create_bear)

    assert response_delete.status_code == 200, "Response status code does not match expected"
    assert response_delete.text == "OK", "Response text does not match expected"
    # Запрос за получение медведя
    response_get = PreparedRequests().getSpecificBear(prepare_and_create_bear)

    assert response_get.status_code == 200, "Response status code does not match expected"
    assert response_get.text == "EMPTY", "Response text does not match expected"

# Тест на удаление всех медведей
def test_delete_all_bear(prepare_and_create_bear):
    # Запроса на удаление всех медведей
    response_delete = PreparedRequests().deleteAllBear()

    assert response_delete.status_code == 200, "Response status code does not match expected"
    assert response_delete.text == "OK", "Response text does not match expected"
    # Запрос на получение всех медведей
    response_get = PreparedRequests().getAllBears()

    bears = json.loads(response_get.text)
    # Проверка, что список медведй пустой
    assert len(bears) == 0, "Stored on server bears number not equal 0"
