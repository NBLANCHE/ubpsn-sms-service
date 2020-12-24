import os

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from charity_user.models import CharityUser
from message.models import Message, MessageStatus, IncomingSms

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

        return MessagingResponse()
