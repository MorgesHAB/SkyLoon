#!/usr/bin/python
# coding=utf-8
 
#############################################################################################################
### Copyright by Joy-IT
### Published under Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
### Commercial use only after permission is requested and granted
### Programme traduit par Go tronic
###
### KY-053 Analog Digital Converter - Raspberry Pi Python Code Example
###
#############################################################################################################
 
# Ce code utilise les librairies Python ADS1115 et I2C pour la Raspberry Pi
# Ces librairies sont publiées sous licence BSD sur le lien ci-dessous
# [https://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code]
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
 
# Les modules nécessaires sont importés et mis en place
import time, signal, sys, os
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Les variables utilisées sont initialisées
delayTime = 0.5 # in Sekunden
 
# attribution d'adresse ADS1x15 ADC
 
ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit
 
# Choix du gain
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V
 
# Choix de la fréquence d'échantillonnage ADC (SampleRate)
# sps = 8    # 8 échantillons par seconde
# sps = 16   # 16 échantillons par seconde
# sps = 32   # 32 échantillons par seconde
sps = 64   # 64 échantillons par seconde
# sps = 128  # 128 échantillons par seconde
# sps = 250  # 250 échantillons par seconde
# sps = 475  # 475 échantillons par seconde
# sps = 860  # 860 échantillons par seconde
 
# choix du canal ADC (1-4)
adc_channel_0 = 0    # Channel 0
adc_channel_1 = 1    # Channel 1
adc_channel_2 = 2    # Channel 2
adc_channel_3 = 3    # Channel 3
 
# initialisation du convertisseur
adc = ADS1x15(ic=ADS1115)
 
Button_PIN = 24
GPIO.setup(Button_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
#############################################################################################################
 
# ########
# boucle de programme principale
# ########
# Le programme lit les tensions en entrées et les transmet à la console.
 
try:
        while True:
                #Les valeurs de tension sont enregistrées
                adc0 = adc.readADCSingleEnded(adc_channel_0, gain, sps)
                adc1 = adc.readADCSingleEnded(adc_channel_1, gain, sps)
                adc2 = adc.readADCSingleEnded(adc_channel_2, gain, sps)
                adc3 = adc.readADCSingleEnded(adc_channel_3, gain, sps)
 
                # Envoi vers la console
                print "Lecture Channel 0:", adc0, "mV "
                print "Lecture Channel 1:", adc1, "mV "
                print "Lecture Channel 2:", adc2, "mV "
                print "Lecture Channel 3:", adc3, "mV "
                print "---------------------------------------"
 
                # Reset + Delay
                button_pressed = False
                time.sleep(delayTime)
 
 
 
except KeyboardInterrupt:
        GPIO.cleanup()