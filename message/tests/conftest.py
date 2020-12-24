import os

import pytest

from message.tests.test_end_to_end.client import Client

test_user = {"phone_number": "4168716985", "name": "Test User"}


@pytest.fixture(scope="session", autouse=True)
def client() -> Client:
    env_name = os.environ.get("STAGE", "LOCAL")
    return Client(env_name)


@pytest.fixture(scope="session", autouse=True)
def existing_user(client: Client):

    try:
        return client.get_charity_user_by_phone_number(test_user["phone_number"])
    except Exception:
        r = client.create_charity_user(test_user["name"], test_user["phone_number"])
        assert 201 == r.status_code
        return r.json()
