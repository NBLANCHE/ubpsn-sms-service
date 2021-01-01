import os

import pytest

from tests.test_end_to_end.client import Client

test_user = {"phone_number": "4168716985", "name": "Test User"}

test_topic = {"name": "Test Topic"}


@pytest.fixture(scope="session", autouse=True)
def client() -> Client:
    env_name = os.environ.get("STAGE", "LOCAL")
    return Client(env_name)


@pytest.fixture(scope="session", autouse=True)
def existing_user(client: Client):
    try:
        user = client.get_charity_user_by_phone_number(test_user["phone_number"])
        for topic_id in user["subscribed_newsletter_topics"]:
            client.unsubscribe_user_to_newsletter_topic(
                user["phone_number"], client.get_newsletter_topic(topic_id)['name']
            )
        return client.get_charity_user_by_phone_number(test_user["phone_number"])
    except Exception:
        r = client.create_charity_user(test_user["name"], test_user["phone_number"])
        assert r.status_code == 201
        return r.json()


@pytest.fixture(scope="session", autouse=True)
def existing_topic(client: Client):
    try:
        return client.get_newsletter_topic_by_name(test_topic["name"])
    except Exception:
        r = client.create_newsletter_topic(test_topic["name"])
        assert r.status_code == 201
        return r.json()
