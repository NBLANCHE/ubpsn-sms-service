import json

import requests
from dicttoxml import dicttoxml

URL_CONFIG = {
    "LOCAL": "http://localhost:8000",
}


class Client:
    def __init__(self, stage: str):
        self.url = URL_CONFIG.get(stage)

    def get(self, url_suffix):
        return requests.get(self.url + url_suffix)

    def post(self, url_suffix, data=None, headers=None):
        if headers is None:
            headers = {"content-type": "application/json"}
        return requests.post(self.url + url_suffix, data=data, headers=headers)

    def put(self, url_suffix, data=None):
        if data is None:
            data = {}
        return requests.put(
            self.url + url_suffix,
            data=data,
            headers={"content-type": "application/json"},
        )

    def delete(self, url_suffix):
        return requests.delete(self.url + url_suffix)

    ####################################################################################################################
    def get_messages(self):
        return self.get("/message/")

    def get_message_by_message_text(self, message_text):
        r = self.get_messages()
        return list(
            filter(lambda message: message["message"] == message_text, r.json())
        )[0]

    def create_message(self, user_id, text):
        message = {"message": text, "message_user_id": user_id}
        return self.post("/message/", data=json.dumps(message))

    def get_charity_users(self):
        return self.get("/charity_user/")

    def get_charity_user_by_phone_number(self, phone_number):
        r = self.get_charity_users()
        users = r.json()
        return list(filter(lambda user: user["phone_number"] == phone_number, users))[0]

    def create_charity_user(self, name, phone_number):
        user = {"name": name, "phone_number": phone_number}
        return self.post("/charity_user/", data=json.dumps(user))

    def receive_sms_message(self, from_phone_number, text):
        sms_message = {
            "ToCountry": "US",
            "ToState": "AR",
            "SmsMessageSid": "SM0cedfbcb5c0f86a93f12b1d30f5d7932",
            "NumMedia": "0",
            "ToCity": "BALD KNOB",
            "FromZip": "",
            "SmsSid": "SM0cedfbcb5c0f86a93f12b1d30f5d7932",
            "FromState": "ON",
            "SmsStatus": "received",
            "FromCity": "TORONTO",
            "Body": text,
            "FromCountry": "CA",
            "To": "+15015309885",
            "ToZip": "72010",
            "NumSegments": "1",
            "MessageSid": "SM0cedfbcb5c0f86a93f12b1d30f5d7932",
            "AccountSid": "AC56677302c2499214aeecbc8cde20cfb3",
            "From": from_phone_number,
            "ApiVersion": "2010-04-01",
        }

        return self.post(
            "/message/twilio_sms_webhook",
            data=sms_message,
            headers={"content-type": "application/x-www-form-urlencoded"},
        )
