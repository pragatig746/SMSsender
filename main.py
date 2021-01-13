from twilio.rest import Client
import os


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body="Hey!Pragati here",
                     from_='your assigned number',
                     to='other person's number'
                 )

print(message.sid)
