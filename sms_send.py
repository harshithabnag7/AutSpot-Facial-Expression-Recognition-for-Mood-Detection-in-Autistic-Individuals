from twilio.rest import Client
account_sid = "AC67c7e90f107213ca1855d2fd2d1c9e4d"
auth_token = "1ad4093c2c16fe49c02ea8567c9a8484"
client = Client(account_sid, auth_token)
def send_alert(emg_contact):
    message = client.messages.create(body = "Your contact is having an autism  episode", from_ = '+18559254969', to = emg_contact)
    print(message.sid)