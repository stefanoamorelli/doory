#!/usr/bin/env python3
import subprocess
import os
import RPi.GPIO as GPIO
import picamera
import argparse
import base64
import json
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

mood = 3
UNLIKELY = "UNLIKELY"

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
	camera = picamera.PiCamera()
	camera.capture("image.jpg")
	credentials = GoogleCredentials.get_application_default()
	service = discovery.build('vision', 'v1', credentials = credentials)
	with open('image.jpg', 'rb') as image:
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
#		print ( json.dumps(response, indent=4, sort_keys=True))
		os.remove("/home/root/out")
		file_out = open("/home/root/out", "w+")
		file_out.write(json.dumps(response, indent=4, sort_keys=True))
		file_out.close()

#if name == '__main__':
main()

#SURPRISE CHECK
os.system("cat out | grep surpriseLikelihood > response.txt")

with open ("response.txt", "r") as myfile:
	data=myfile.readline()

list_data = data.split(": ")

if UNLIKELY not in list_data[1]:
	mood = 0

#SORROW CHECK
os.system("cat out | grep sorrowLikelihood > response.txt")

with open ("response.txt", "r") as myfile:
	data=myfile.readline()

list_data = data.split(": ")

if UNLIKELY not in list_data[1]:
	mood = 1

#ANGER CHECK
os.system("cat out | grep angerLikelihood > response.txt")

with open ("response.txt", "r") as myfile:
	data=myfile.readline()

list_data = data.split(": ")

if UNLIKELY not in list_data[1]:
	mood = 2

if mood == 0:
	GPIO.output(gpio0, GPIO.HIGH) #FRAGRANCE demo
	os.system("/home/root/script.sh REST on on off")

if mood == 1:
	GPIO.output(gpio1, GPIO.HIGH)
	os.system("/home/root/script.sh REST on off off")

if mood == 2:
	GPIO.output(gpio2, GPIO.HIGH)
	os.system("/home/root/script.sh REST off off on")

if mood == 3:
	GPIO.output(gpio3, GPIO.HIGH)
	os.system("/home/root/script.sh REST off on off")

print(mood)
