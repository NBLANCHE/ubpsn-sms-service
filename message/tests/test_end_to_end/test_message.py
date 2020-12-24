import uuid
from random import randint

from message.tests.test_end_to_end.client import Client


def test_message_create_with_valid_message_should_create(client: Client, existing_user):
    message_text = "Test Message: " + str(uuid.uuid4())
    r = client.create_message(existing_user["id"], message_text)
    assert 201 == r.status_code

    actual_message = client.get_message_by_message_text(message_text)
    assert actual_message["message"] == message_text
    # TODO Fix the user not being sent as part of message


def test_message_create_with_missing_user_should_throw_400(client: Client):
    message_text = "Test Message: " + str(uuid.uuid4())
    r = client.create_message(message_text, 200000)
    assert 400 == r.status_code


def test_twilio_webhook_with_existing_user_should_create_message(
    client: Client, existing_user
):
    message_text = "Test Message: " + str(uuid.uuid4())
    r = client.receive_sms_message(existing_user["phone_number"], message_text)
    assert 201 == r.status_code

    actual_message = client.get_message_by_message_text(message_text)
    assert actual_message["message"] == message_text
    # TODO Fix the user not being sent as part of message


def test_twilio_webhook_with_missing_user_should_create_user_and_message(
    client: Client,
):
    message_text = "Test Message: " + str(uuid.uuid4())
    random_phone_number = str(randint(1000000000, 9999999999))
    r = client.receive_sms_message(random_phone_number, message_text)
    assert 201 == r.status_code

    actual_message = client.get_message_by_message_text(message_text)
    assert actual_message["message"] == message_text
    # TODO Fix the user not being sent as part of message

    actual_user = client.get_charity_user_by_phone_number(random_phone_number)
    assert actual_user["name"] == ""
