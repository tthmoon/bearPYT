import pytest
from requests import Session
from prepared_requests import PreparedRequests

from bear_body import BearBody

def test_server_connect():
    b_body = BearBody.create_bear_body(BearBody.BearTypes.BROWN, "b", 4, kek=4)
    request = PreparedRequests().createBear(b_body)
    response = Session().send(request) 