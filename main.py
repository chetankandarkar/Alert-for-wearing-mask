import conf
from boltiot import Sms, Bolt
import requests
import json, time

myBolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

def readSensor():
     print("Reading LDR sensor value")
     input = myBolt.analogRead("A0")
     data=json.loads(input)
     print("LDR sensor value is " + str(data["value"]))
     return data

def buzzeron():
     output = myBolt.digitalWrite("0", "HIGH")
     return output
def buzzeroff():
     output = myBolt.digitalWrite("0", "LOW")
     return output

data1 = readSensor()
value1 = int(data1["value"])
while True:
     time.sleep(5)
     data2 = readSensor()
     value2 = int(data2["value"])
     value1 = value1 + 100
     if value2<1024:
         buzzeron()
         print("Making Request to Twilio for SMS")
         response=sms.send_sms("Please Don't forget to wear your mask")
         print("response received from Twilio is:" +str(response))
         time.sleep(5)
         buzzeroff()
     value1 = value2