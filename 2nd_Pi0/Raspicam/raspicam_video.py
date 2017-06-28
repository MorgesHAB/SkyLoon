#!/usr/bin/python
#coding=utf-8
# This script will be actived each minute

# First write "sudo apt-get install python3-picamera" on the raspbery pi terminal

# import all the module we will need
import os
import RPi.GPIO as GPIO
import picamera
from random import randrange
import time

# setup the camera with the module picamera
camera=picamera.PiCamera()

try :
	# Now we have the Data, we record the temperature and the humidity on file.txt
	os.chdir("/home/pi/SkyLoon/2nd_Pi0/Raspicam/Data_Films")  # Go to the recorded photos folder 
	random_number = str(randrange(999)) # ***
	# We will name the video with the time when the videos is taking
	Time_video = str(time.strftime('%H%M%S'))
	Name_of_video = Time_video+"_"+random_number+".h264"
	camera.resolution = (640, 480)
	camera.start_recording(Name_of_video)  # take a video
	camera.wait_recording(58)
	camera.stop_recording()   #stop video
				

except KeyboardInterrupt :
  print("Exit")

# ***
# We will name the video with the time of the Pi 0, but if the raspberry Pi reboot,
# the time go back a bit, so it's posssible that the new videos have the same name 
# as the older and so errase the old videos. So we will put a random number after 
# the name of the video in order to never take the risk to have the same name of video  !  