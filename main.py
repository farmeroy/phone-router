import os
from twilio.twiml.voice_response import Dial, VoiceResponse, Say
from dotenv import load_dotenv    
load_dotenv()  

PHONE_NUMBER = os.getenv('PHONE_NUMBER')

response = VoiceResponse()
response.dial(PHONE_NUMBER)
response.say('Goodbye')

print(response)
