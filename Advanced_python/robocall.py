import json
import pprint
import datetime
from pprint import pprint as pp

!pip install --user twilio

# from https://www.twilio.com/docs/voice/tutorials/how-to-make-outbound-phone-calls-python
from twilio.rest import Client
from twilio.twiml.voice_response import Play, VoiceResponse

### To run this code from your free Google Colaboratory account (colab.research.google.com)
###   Uncomment the three lines below  and comment out the last.
#from google.colab import files # uncomment for Google Colab
#uploaded = files.upload() # uncomment for Google Colab
#uploaded = list( uploaded.values() ).pop().decode('utf-8') # uncomment for Google Colab
from ipywidgets import FileUpload
uploaded = FileUpload(multiple=False)
uploaded

#auth_pers = json.loads( list( uploaded.values() ).pop().decode('utf-8') )['twilio'] # uncomment for Google Colab
auth_pers = json.loads(uploaded.data[0])
twilioAccount = auth_pers['twilio']['accountSID']
twilioToken = auth_pers['twilio']['authToken']
twilioPhoneRobo = auth_pers['twilio']['phoneNumberTwilio']
twilioPhoneReal = auth_pers['twilio']['phoneNumberPersonal']
client = Client(twilioAccount, twilioToken) # 🚀

#Send message
message = client.messages.create(
                              from_=twilioPhoneRobo,
                              to=twilioPhoneReal,
                              body='Mr. Watson — Come here — I want to see you.',
                          ) # 🚀
print(message.sid)

message = client.messages.create(
                              from_=twilioPhoneRobo,
                              to=twilioPhoneReal,
                              body='FYI, the time right now is {}.'.format( datetime.datetime.now().time() ),
                          ) # 🚀
print(message.sid)

scriptURL = 'http://demo.twilio.com/docs/voice.xml'
call = client.calls.create(
                        url=scriptURL,
                        to=twilioPhoneReal,
                        from_=twilioPhoneRobo,
                        send_digits='3212333w222w399w3212333w322321', # 🎵Mary Had a Little Lamb🎵                                                                      # w means wait  for 0.5 seconds
                    ) # 🚀
print(call.sid)

#MAking own call message

response = VoiceResponse()
response.say('beep', voice='man', loop=7)
response.say('This is your wake up call, and language lesson', voice='man', language='en-GB')
response.say('The hat on the head', voice='man', language='en-US')
response.say('Le chapeau sur la tête', voice='woman', language='fr-FR')
response.say('A man, a plan, a canal, Panama', voice='man', language='en-US')
response.say('Een man, een plan, een kanal, Panama', voice='woman', language='nl-NL')
response.play(digits="3w3w3w1w53w1w53ww7w7w7w8w53w1w53") ##  🎵Imperial Death March🎵
response.play('http://demo.twilio.com/docs/classic.mp3', loop=2)
response.hangup()

print(response) # paste the output of this

scriptURL = 'http://demo.twilio.com/docs/voice.xml'
call = client.calls.create(
                        url=scriptURL,
                        to=twilioPhoneReal,
                        from_=twilioPhoneRobo,
                        send_digits='3212333w222w399w3212333w322321', # 🎵Mary Had a Little Lamb🎵                                                                      # w means wait  for 0.5 seconds
                    ) # 🚀
print(call.sid)


