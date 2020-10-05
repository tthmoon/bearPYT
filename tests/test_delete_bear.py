import json

import pytest
from requests import Session
from bear_server.prepared_requests import PreparedRequests

from bear_server.bear_body import BearBody


@pytest.fixture(autouse=True)
def prepare_and_create_bear():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.POLAR, "test", 15.2)

    request = PreparedRequests().createBear(b_body)
    response_post = Session().send(request)
    assert response_post.status_code == 200

    bear_id = int(response_post.text)

    return bear_id


def test_delete_specific_bear(prepare_and_create_bear):
    request = PreparedRequests().deleteSpecificBear(prepare_and_create_bear)
    response_delete = Session().send(request)
    assert response_delete.status_code == 200
    assert response_delete.text == "OK"

    request = PreparedRequests().getSpecificBear(prepare_and_create_bear)
    response_get = Session().send(request)
    assert response_get.status_code == 200
    assert response_get.text == "EMPTY"


def test_delete_all_bear(prepare_and_create_bear):
    request = PreparedRequests().deleteAllBear()
    response_delete = Session().send(request)
    assert response_delete.status_code == 200
    assert response_delete.text == "OK"

    request = PreparedRequests().getAllBears()
    response_get = Session().send(request)
    bears = json.loads(response_get.text)
    assert len(bears) == 0
