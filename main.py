import os
from flask import Flask
from twilio.twiml.voice_response import Dial, VoiceResponse
from dotenv import load_dotenv    
load_dotenv()  

TARGET_PHONE_NUMBER = os.getenv('TARGET_PHONE_NUMBER')
account_sid = os.getenv('TWILIO_ACCOUNT_SID')    
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def call():
    response = VoiceResponse()
    response.dial(TARGET_PHONE_NUMBER)

    return str(response)

