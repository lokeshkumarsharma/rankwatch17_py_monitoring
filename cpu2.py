"""To get the CPU,RAM and Disk Usage
first install psutil library with the help of pip
pip install psutil"""

import os
import psutil
from time import time, sleep

def start_moitoring():
 #Monitoring the system states.
  disk_usage = []
  cpu_usage = []
  ram_usage = []

  while True:
  #creation of arrays to store  the usage	
    sleep(5)
    r1 = psutil.virtual_memory()						#checks whether the time difference is 5 seconds or not
    d1 = psutil.disk_usage('/')							#get the complete information about RAM like free and used 
    d = psutil.disk_usage('/').used						#get the complete information about storage like free and used
    c = psutil.cpu_percent()
    r = psutil.virtual_memory().used
	
		#print the usage 
    print "CPU Core :", psutil.cpu_count()
    print "RAM Usage", r1
    print "Disk Usage", d1
    print "CPU Usage", c
    print("\n")
    disk_usage.append(d)  #store the used part of disk in an array
    cpu_usage.append(c)  #store the used percent  of cpu in an array
    ram_usage.append(r)  #store the memory in an array

    if len(disk_usage) % 6 == 0:
	#usage for last 30 seconds
      print"last 30 seconds"
	  #add the usage of last 30 seconds and take the average
      print "Average Disk :", sum(disk_usage[-6:]) / 6		
      print "Average CPU :", sum(cpu_usage[-6:]) / 6
      print "Average RAM :", sum(ram_usage[-6:]) / 6

    if len(disk_usage) % 12 == 0:
	#usage for last 30 seconds
      print"last 1 minutes"
	  #add the usage of last 1 minute and take the average
      print "Average Disk :", sum(disk_usage[-12:]) / 12
      print "Average CPU :", sum(cpu_usage[-12:]) / 12
      print "Average RAM :", sum(ram_usage[-12:]) / 12

    if len(disk_usage) % 30 == 0:
	#usage for last 30 seconds
      print"last 5 minutes"
	  #add the usage of last 5 minutes and take the average
      print "Average Disk :", sum(disk_usage) / 60
      print "Average CPU :", sum(cpu_usage) / 60
      print "Average RAM :", sum(ram_usage) / 60
      # Reset usage.
      disk_usage = []
      cpu_usage = []
      ram_usage = []


if __name__ == '__main__':
  start_moitoring()