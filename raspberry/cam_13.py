#!/usr/bin/env python3
import os
import RPi.GPIO as GPIO
import picamera
import argparse
import base64
import json
import time
import urllib.request
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

UNLIKELY = "UNLIKELY"

#Definitions of the moods
#0: SURPRISE
#1: SORROW
#2: ANGER
#3: JOY
#4: NORMAL

GPIO.setmode(GPIO.BCM)
gpio0 =12
gpio1 =16
gpio2 =20
gpio3 =21
GPIO.setup(gpio0, GPIO.OUT)
GPIO.setup(gpio1, GPIO.OUT)
GPIO.setup(gpio2, GPIO.OUT)
GPIO.setup(gpio3, GPIO.OUT)

def main():
	
  contents1 = urllib.request.urlopen("http://188.166.111.117/doory/check1.php").read()
  while contents1 == "no":
    time.sleep(1)
    contents1 = urllib.request.urlopen("http://188.166.111.117/doory/check1.php").read()

  responses = ["VERY_LIKELY", "LIKELY", "POSSIBLE"]
  likelihs = ["surpriseLikelihood", "sorrowLikelihood", "angerLikelihood", "joyLikelihood"]
  mood_statistic = [0, 0, 0, 0, 0]
  
  camera = picamera.PiCamera()
  
  for picture in range(0,10):
    #Get an image
    camera_path = "image"+str(picture)+".jpg"
    camera.capture(camera_path)

  for picture in range(0,10):
    #Google API for mood recognition	
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials = credentials)
    image_path = 'image'+str(picture)+'.jpg'
    with open(image_path, 'rb') as image:
      image_content = base64.b64encode(image.read())
      service_request = service.images().annotate(body={
		  	'requests': [{
		  		'image': {
		  			'content': image_content.decode('UTF-8')
		  		},
		  		'features': [{
		  			'type': 'FACE_DETECTION',
		  			'maxResults': 10
		  		}]
		  	 }]
		  })
      response = service_request.execute()
      #print ( json.dumps(response, indent=4, sort_keys=True))
      os.remove("/home/root/out")
      file_out = open("/home/root/out", "w+")
		
	  	#Response redirected in file out
      file_out.write(json.dumps(response, indent=4, sort_keys=True))
      file_out.close()
    
    #Check of the mood
    mood = 4
    mood_index = 3
    for i in range(0,4):
      #Filter the response for each mood
      command = "cat out | grep " + likelihs[i] + " > response.txt" 
      os.system(command)
      
      with open("response.txt", "r") as myfile:
        data = myfile.readline()
        
      list_data = data.split(": ")      
      #print(data)

      #Assigning the mood with the highest likelihood      
      for j in range(0,3):
        temp = list_data[1].replace(",","")
        temp = temp.replace("\"", "")
        temp = temp.replace("\n", "")
        #print(temp + responses[j])
        if responses[j] == temp:
          #print("OK!")
          if j < mood_index:
            mood = i
            mood_index = j
    
    mood_statistic[mood] = mood_statistic[mood]+1
  
  #Analysis on the data
  maxim = -1;
  for i in range(0,5):
    #print(mood_statistic[i])
    if(mood_statistic[i] > maxim):
      mood = i;
      maxim = mood_statistic[i]
    
  contents = urllib.request.urlopen("http://188.166.111.117/doory/get.php").read()

  if contents == 'yes':
  #Action based on mood
    if mood == 0:
      #GPIO.output(gpio0, GPIO.HIGH) #FRAGRANCE demo
      #os.system("/home/root/script.sh REST on on off")
      os.system("aplay Happy.wav")
    
    if mood == 1:
      #GPIO.output(gpio1, GPIO.HIGH) #FRAGRANCE demo
      #os.system("/home/root/script.sh REST on off off")
      os.system("aplay Sorrow.wav")
      
    if mood == 2:
      #GPIO.output(gpio2, GPIO.HIGH) #FRAGRANCE demo
      #os.system("/home/root/script.sh REST off off on")
      os.system("aplay Angry.wav")
      
    if mood == 3:
      #GPIO.output(gpio3, GPIO.HIGH) #FRAGRANCE demo
      #os.system("/home/root/script.sh REST off on off")
      os.system("aplay Happy.wav")

    if mood == 4:
      #GPIO.output(gpio3, GPIO.HIGH) #FRAGRANCE demo
      #os.system("/home/root/script.sh REST off on off")
      os.system("aplay Neutral.wav")
    
  print(mood)

  if mood == 0:
    #GPIO.output(gpio0, GPIO.HIGH) #FRAGRANCE demo
    #os.system("/home/root/script.sh REST on on off")
    contents = urllib.request.urlopen("https://maker.ifttt.com/trigger/surprise/with/key/plrPhCevofu9SYNLoWydfpbV4BDJNYTH8vqWQbCCJo_").read()
    
  if mood == 1:
    #GPIO.output(gpio1, GPIO.HIGH) #FRAGRANCE demo
    #os.system("/home/root/script.sh REST on off off")
    contents = urllib.request.urlopen("https://maker.ifttt.com/trigger/sorrow/with/key/plrPhCevofu9SYNLoWydfpbV4BDJNYTH8vqWQbCCJo_").read()
    
  if mood == 2:
    #GPIO.output(gpio2, GPIO.HIGH) #FRAGRANCE demo
    #os.system("/home/root/script.sh REST off off on")
    contents = urllib.request.urlopen("https://maker.ifttt.com/trigger/angry/with/key/plrPhCevofu9SYNLoWydfpbV4BDJNYTH8vqWQbCCJo_").read()
     
  if mood == 3:
    #GPIO.output(gpio3, GPIO.HIGH) #FRAGRANCE demo
    #os.system("/home/root/script.sh REST off on off")
    contents = urllib.request.urlopen("https://maker.ifttt.com/trigger/happy/with/key/plrPhCevofu9SYNLoWydfpbV4BDJNYTH8vqWQbCCJo_").read()

  if mood == 4:
    #GPIO.output(gpio3, GPIO.HIGH) #FRAGRANCE demo
    #os.system("/home/root/script.sh REST off on off")
    contents = urllib.request.urlopen("https://maker.ifttt.com/trigger/neutral/with/key/plrPhCevofu9SYNLoWydfpbV4BDJNYTH8vqWQbCCJo_").read()

  
#if name == '__main__':
main()

