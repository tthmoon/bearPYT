import json

import pytest
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody


# Фикстура для создания медведя, передает в тест id и тело медведя (как объект json)
@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)
    b_body_json = json.loads(b_body)

    response_post = PreparedRequests().createBear(b_body)
    assert response_post.status_code == 200, "Response status code does not match expected"

    bear_id = int(response_post.text)

    return bear_id, b_body_json

# Тест на изменение имени
def test_change_bear_name_positive(prepare_and_create_bear):
    bear_id, b_body_json = prepare_and_create_bear
    b_body_json["bear_name"] = "newTestName"
    b_body = json.dumps(b_body_json)
    # Запрос на создание медведя
    response_send = PreparedRequests().updateSpecificBear(bear_id, b_body)

    assert response_send.status_code == 200, "Response status code does not match expected"
    assert response_send.text == "OK", "Response text does not match expected"
    # Запрос на получение медведя
    response_get = PreparedRequests().getSpecificBear(bear_id)

    assert response_get.status_code == 200, "Response status code does not match expected"
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper(), \
        "Created bear type does not match expected"
    assert response_get.json()["bear_id"] == bear_id, "Created bear id does not match expected"
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper(), \
        "Created bear name does not match expected"
    assert response_get.json()["bear_age"] == b_body_json["bear_age"], "Created bear age does not match expected"

