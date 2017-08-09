#coding=utf-8

import subprocess
import time

# Define vrariable how would count the number of GPS Data
Nbr_Data = 0
# Define the number of Data you want to record in 1 min
Nbr_Data_per_Minute = 3
Time_between_each_recorded_data = int(60 / Nbr_Data_per_Minute)  # 60 because 1 min

try :
	while Nbr_Data < Nbr_Data_per_Minute :
		Tension = subprocess.check_output(["/opt/vc/bin/vcgencmd measure_volts | cut -c6-9"], shell=True)[:-1]
		Tension_ = str(Tension)
		TIME1 = time.strftime("%H-%M-%S")    # take the Pi0 time 
		with open("Tension.txt","a") as fichier :
			print >> fichier, Tension_+" at "+TIME1
		Temp_CPU = subprocess.check_output(["/opt/vc/bin/vcgencmd measure_temp | cut -c6-9"], shell=True)[:-1]
		TIME2 = time.strftime("%H-%M-%S")    # take the Pi0 time 
		Temp_ = str(Temp_CPU)
		with open("Temp_CPU.txt","a") as fichier2 :
			print >> fichier2, Temp_+" at "+TIME2
		time.sleep(Time_between_each_recorded_data)
		Nbr_Data+=1
except :
	TIME3 = time.strftime("%H-%M-%S")    # take the Pi0 time 
	with open("Tension.txt","a") as fichier3 :
		print >> fichier3, " ERROR at "+TIME3


