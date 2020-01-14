#!/usr/bin/env python
import getpass
import sys
import telnetlib
#import time
import os
#import itertools
import gzip
import csv

#   Introduceti user si pass
user = raw_input("Introduceti username: ")
password = getpass.getpass()

#timestamp = time.strftime("%d" + "-" + "%m" + "-" + "%Y")

loops = open("loopbacks")

for line in loops:
    try:
        print "Se acceseaza : " + (line)
        HOST = line.strip()
        tn = telnetlib.Telnet(HOST)

        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")

        tn.write("terminal length 0\n")
	tn.write("show run | i host\n")
        tn.write("show ip int brief | e una|Loop\n")
	tn.write("\n")
        tn.write("exit\n")

        readoutput = tn.read_all()
        saveoutput = open("logfile", "a")
        saveoutput.write(readoutput)
        saveoutput.close
	
	print readoutput

    except:
        print("Hostul " + str(HOST) + " e down.")

f=open("logfile", "r")

os.system("cat logfile | grep -E -o 'FastEthernet([0-9])\/([0-9])||( R-(.))' > iface")
os.system("cat logfile | grep -E -o '(25[0-5]|2[0-4][0-9]|1[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[1]?[0-9][0-9]?)||( R-(.))' > ipaddr")

iface=open("iface", "r")
ipaddr=open("ipaddr", "r")

with open ("output.csv", "w") as output:
	writer = csv.writer(output)

	writer.writerow(['Interface', 'IP address'])
	
	for line1, line2 in zip(iface, ipaddr):
		writer.writerow([line1.strip(), line2.strip()])

