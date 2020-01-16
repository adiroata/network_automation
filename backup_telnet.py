#!/usr/bin/env python

import getpass
import sys
import telnetlib
import time

#   Introduceti user si pass
user = raw_input("Introduceti username: ")
password = getpass.getpass()

timestamp = time.strftime("%d" + "-" + "%m" + "-" + "%Y")

loops = open("loopbacks")

for line in loops:
    try:
        print "Se acceseaza : " + (line)
        HOST=line.strip()
        tn=telnetlib.Telnet(HOST)

        tn.read_until("Username: ")
        tn.write(user + "\n")
        if password:
            tn.read_until("Password: ")
            tn.write(password + "\n")

        tn.write("terminal length 0\n")
	tn.write("show run\n")
        tn.write("exit\n")

        readoutput=tn.read_until("exit", 5)
        saveoutput=open("config_host_" + HOST + "_" + timestamp, "w")
        saveoutput.write(readoutput)
        saveoutput.close
#	print readoutput

    except:
        print("Hostul " + str(HOST) + " e down.")


