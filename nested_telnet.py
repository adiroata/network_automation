#!/usr/bin/env python
import getpass
import sys
import telnetlib
import time
#import os
#import itertools

host_pe = raw_input ("Introduceti adresa PE: ")
user_pe = raw_input("Introduceti username PE: ")
password_pe = getpass.getpass()

user_cpe = raw_input("Introduceti username CPE: ")
password_cpe = getpass.getpass()

f=open("lista-adrese-cpe", "r")

for line in f:
    try:
        print("Se acceseaza CPE-ul " + str(line.strip()))

#   Conectarea pe PE
        telnet  = telnetlib.Telnet(host_pe)
        telnet.read_until("Username: ", 5)
        telnet.write(user_pe + "\r")
        telnet.read_until("Password: ", 5)
        telnet.write(password_pe + "\r")

#   Conectarea pe CPE
        telnet.write("telnet " + str(line.strip()) + " /vrf nume_vrf\r")
        telnet.read_until("username: ", 5)
        telnet.write(user_cpe + "\r")
        telnet.read_until("password: ", 5)
        telnet.write(password_cpe + "\r")
        telnet.write("\n")
        telnet.write("display interface description\r")
        telnet.write("quit\n")

#   Se salveaza output-ul
        readoutput = telnet.read_until("quit", 10)
        saveoutput = open("output_telnet", "ab")
        saveoutput.write(readoutput)
        saveoutput.close
        print readoutput
    except:
        print("Hostul " + str(line.strip()) + " e down.")
