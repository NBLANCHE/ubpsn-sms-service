import os
import re

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from charity_user.models import CharityUser
from message.models import Message, MessageStatus, IncomingSms
from newsletter_topic.models import NewsletterTopic

should_send = True


class MessageService:
    def __init__(self):
        twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        twilio_phone_number = os.getenv("TWILIO_NUMBER")
        self.twilio = Client(twilio_account_sid, twilio_auth_token)
        self.twilio_phone_number = twilio_phone_number

    def send_message(self, message: Message):
        message.message_status = MessageStatus.CREATED
        message.save()
        try:
            if should_send:
                self.twilio.messages.create(
                    to=message.charity_user.phone_number,
                    from_=self.twilio_phone_number,
                    body=message.message,
                )

            message.message_status = MessageStatus.SENT
        except TwilioRestException as e:
            message.message_status = MessageStatus.FAILED
            message.save()

        return message

    def receive_message(self, incoming_sms: IncomingSms):
        phone_number = incoming_sms.from_number
        try:
            charity_user = CharityUser.objects.get(phone_number=phone_number)
        except:
            charity_user = CharityUser(phone_number=phone_number)
            charity_user.save()

        message = Message()
        message.status = MessageStatus.DELIVERED
        message.message = incoming_sms.body
        message.charity_user = charity_user
        message.save()
        message = str(message.message)

        match_object = re.search("^subscribe (.*)", message)
        if match_object:
            topic_name = match_object.group(1)
            topic = list(NewsletterTopic.objects.filter(name=topic_name))[0]
            charity_user.subscribed_newsletter_topics.add(topic)
            charity_user.save()
            return MessagingResponse()

        match_object = re.search("^unsubscribe (.*)", message)
        if match_object:
            topic_name = match_object.group(1)
            topic = list(NewsletterTopic.objects.filter(name=topic_name))[0]
            charity_user.subscribed_newsletter_topics.remove(topic)
            charity_user.save()
            return MessagingResponse()

        return MessagingResponse()
