from random import randint
from uuid import uuid4

from tests.test_end_to_end.client import Client


def test_create_user_with_valid_user_should_create_user(
    client: Client,
):
    user = create_test_user()
    client.create_charity_user(user["name"], user["phone_number"])

    actual_user = client.get_charity_user_by_phone_number(user["phone_number"])
    assert user.items() <= actual_user.items()


def test_subscribe_user_with_missing_should_create_user_and_subscribe(
    client: Client,
    existing_topic,
):
    phone_number = create_test_user()["phone_number"]
    user = {"name": "", "phone_number": phone_number}

    client.subscribe_user_to_newsletter_topic(
        user["phone_number"], existing_topic["name"]
    )
    actual_user = client.get_charity_user_by_phone_number(user["phone_number"])
    assert user.items() <= actual_user.items()
    assert (
        actual_user["subscribed_newsletter_topics"][0].items() <= existing_topic.items()
    )


def test_unsubscribe_user_with_missing_should_create_user(
    client: Client,
    existing_topic,
):
    phone_number = create_test_user()["phone_number"]
    user = {
        "name": "",
        "phone_number": phone_number,
        "subscribed_newsletter_topics": [],
    }

    client.unsubscribe_user_to_newsletter_topic(
        user["phone_number"], existing_topic["name"]
    )
    actual_user = client.get_charity_user_by_phone_number(user["phone_number"])
    assert user.items() <= actual_user.items()


def test_subscribe_unsubscribe_user_with_existing_user_should_subscribe_and_unsubscribe(
    client: Client,
    existing_user,
    existing_topic,
):
    actual_user = client.get_charity_user_by_phone_number(existing_user["phone_number"])
    assert len(actual_user["subscribed_newsletter_topics"]) == 0

    client.subscribe_user_to_newsletter_topic(
        existing_user["phone_number"], existing_topic["name"]
    )
    actual_user = client.get_charity_user_by_phone_number(existing_user["phone_number"])
    assert (
        actual_user["subscribed_newsletter_topics"][0].items() <= existing_topic.items()
    )

    client.unsubscribe_user_to_newsletter_topic(
        existing_user["phone_number"], existing_topic["name"]
    )
    actual_user = client.get_charity_user_by_phone_number(existing_user["phone_number"])
    assert len(actual_user["subscribed_newsletter_topics"]) == 0


def create_test_user():
    return {
        "name": "Test User " + str(uuid4()),
        "phone_number": str(randint(1000000000, 9999999999)),
    }
