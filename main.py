from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio import twiml

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACb3fcadd62030de6cfad6519e3e377cf1"
auth_token = "9f5f8f07f6e7c9a2b2b2c3c568a94b83"
client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18775543119',
#                      to='+18568853298'
#                  )

# print(message.sid)

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']
    print(from_number)
    print(to_number)
    print(body)

    # Start our TwiML response
    resp = twiml.Response()
    resp.message("This is a Wordle score")
    return str(resp)
#     if body.startswith('Wordle'):
#         message = client.messages.create(
#         from_='+18775543119',
#         body='This is a wordle score',
#         to='+18568853298'
# )
#     else:
#         message = client.messages.create(
#         from_='+18775543119',
#         body='This could be anything',
#         to='+18568853298'
# )

    # Determine the right reply for this message
    # if body.startswith('Wordle'):
    #     resp.message("This is a Wordle score")
    # else:
    #     resp.message("This could be anything")
    
    # resp.redirect("https://demo.twilio.com/welcome/sms/reply")

    # return str(resp)

if __name__ == "__main__":
    app.run(debug=True)


# message = client.messages.create(
#   from_='+18775543119',
#   body='This is a wordle score',
#   to='+18568853298'
# )

# print(message.sid)


