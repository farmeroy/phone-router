import os
from twilio.twiml.voice_response import Dial, VoiceResponse, Say
from dotenv import load_dotenv    
load_dotenv()  

TARGET_PHONE_NUMBER = os.getenv('TARGET_PHONE_NUMBER')

response = VoiceResponse()
response.dial(TARGET_PHONE_NUMBER)
response.say('Goodbye')

print(response)
