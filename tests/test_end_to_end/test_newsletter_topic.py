from uuid import uuid4

from tests.test_end_to_end.client import Client


def test_create_newsletter_topic_with_valid_topic_should_create_topic(
    client: Client,
):
    name = "Test Newsletter Topic " + str(uuid4())
    client.create_newsletter_topic(name)

    topic = client.get_newsletter_topic_by_name(name)
    assert name == topic["name"]
