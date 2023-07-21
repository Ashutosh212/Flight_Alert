from twilio.rest import Client

TWILIO_SID = "ACd3b525f00773cd696412e10baf74b75c"
TWILIO_AUTH_TOKEN = "32a8b3fbdc256a39fa1ba60fd845cee3"
TWILIO_VIRTUAL_NUMBER = "+15856202152"
TWILIO_VERIFIED_NUMBER = "+919334450763"



class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
