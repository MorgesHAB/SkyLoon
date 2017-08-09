#coding=utf-8

import subprocess
import time

try :
	while True :
		Tension = subprocess.popen(["/opt/vc/bin/vcgencmd", "measure_volts"])
		Tension_ = str()
		TIME1 = time.strftime("%H-%M-%S")    # take the Pi0 time 
		with open("Tension.txt","a") as fichier :
			print >> fichier, Tension_+" at "+TIME1
		Temp_CPU = subprocess.popen(["/opt/vc/bin/vcgencmd", "measure_temp"])
		TIME2 = time.strftime("%H-%M-%S")    # take the Pi0 time 
		Temp_ = str()
		with open("Temp_CPU.txt","a") as fichier2 :
			print >> fichier2, Temp_+" at "+TIME2
		time.sleep(20)
except :
	TIME3 = time.strftime("%H-%M-%S")    # take the Pi0 time 
	with open("Tension.txt","a") as fichier3 :
	print >> fichier3, " ERROR at "+TIME3


