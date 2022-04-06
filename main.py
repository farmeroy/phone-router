import os
from flask import Flask
from twilio.twiml.voice_response import Dial, VoiceResponse
from dotenv import load_dotenv    
load_dotenv()  

TARGET_PHONE_NUMBER = os.getenv('TARGET_PHONE_NUMBER')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def call():
    response = VoiceResponse()
    response.dial(TARGET_PHONE_NUMBER)

    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
