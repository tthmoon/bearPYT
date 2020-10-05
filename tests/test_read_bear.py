import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody


@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)
    b_body_json = json.loads(b_body)

    request = PreparedRequests().createBear(b_body)
    response_post = Session().send(request)
    assert response_post.status_code == 200

    bear_id = int(response_post.text)

    return bear_id, b_body_json


def test_read_specific_bear(prepare_and_create_bear):
    bear_id, b_body_json = prepare_and_create_bear
    request = PreparedRequests().getSpecificBear(bear_id)
    response_get = Session().send(request)
    assert response_get.status_code == 200
    assert response_get.json()["bear_type"] == b_body_json["bear_type"].upper()
    assert response_get.json()["bear_id"] == bear_id
    assert response_get.json()["bear_name"] == b_body_json["bear_name"].upper()
    assert response_get.json()["bear_age"] == b_body_json["bear_age"]


def test_read_all_bear(prepare_and_create_bear):
    request = PreparedRequests().getAllBears()
    response_get = Session().send(request)
    bears = json.loads(response_get.text)
    assert len(bears) != 0
