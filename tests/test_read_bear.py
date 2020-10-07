import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody

# Фикстура для очистки всех медведй, после создания медведя, передает в тест id и тело медведя (как объект json)
@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    response_delete = PreparedRequests().deleteAllBear()

    assert response_delete.status_code == 200, "Response status code does not match expected"

    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)
    b_body_json = json.loads(b_body)

    response_post = PreparedRequests().createBear(b_body)

    assert response_post.status_code == 200, "Response status code does not match expected"

    bear_id = int(response_post.text)

    return bear_id, b_body_json

# Тест на чтение определенного медведя
def test_read_specific_bear(prepare_and_create_bear):
    bear_id, b_body_json = prepare_and_create_bear
    # Запрос на получение медведя
    response_get = PreparedRequests().getSpecificBear(bear_id)
    # Проверка тела медведя
    assert response_get.status_code == 200, "Response status code does not match expected"
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper(), \
        "Created bear type does not match expected"
    assert response_get.json()["bear_id"] == bear_id, "Created bear id does not match expected"
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper(), \
        "Created bear name does not match expected"
    assert response_get.json()["bear_age"] == b_body_json["bear_age"], "Created bear age does not match expected"

# Тетс на чтение всех медведей
def test_read_all_bear(prepare_and_create_bear):
    # Получение всех медведей
    response_get = PreparedRequests().getAllBears()
    bears = json.loads(response_get.text)
    # Провека, что список медведей не пустой
    assert len(bears) == 1, "Stored on server bears number not equal 1"
