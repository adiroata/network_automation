#!/usr/bin/env python

import getpass
import telnetlib
import csv
import time

#   Introduceti user si pass
user = raw_input("Introduceti username: ")
password = getpass.getpass()

with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for line in csv_reader:
        try:
            print("Se acceseaza : " + str(line[0]))
            HOST = line[0]
            tn = telnetlib.Telnet(HOST)

            tn.read_until("Username: ")
            tn.write(user + "\n")
            if password:
                tn.read_until("Password: ")
                tn.write(password + "\n")

            tn.write("conf t\n")
            tn.write("ip dhcp excluded-address " + str(line[2]) + "\n")
            tn.write("ip dhcp excluded-address " + str(line[3]) + " " + str(line[4]) + "\n")
            tn.write("ip dhcp pool " + str(line[1]) + "\n")
            tn.write("network " + str(line[5]) + "\n")
            tn.write("default-router " + str(line[2]) + "\n")
            tn.write("end\n")
            tn.write("copy run start\n")
            tn.write("\n")
            tn.read_until("#")
            tn.write("\n")
            tn.write("exit\n")

            readoutput = tn.read_until("exit", 5)
#
#           Pentru logging, decomentati urmatoarele 3 linii.
#
#            saveoutput = open("config_host_" + HOST + "_" + timestamp, "w")
#            saveoutput.write(readoutput)
#            saveoutput.close
            print(readoutput)

        except:
            print("Hostul " + str(HOST) + " e down.")
