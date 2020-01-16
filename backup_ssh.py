#!/usr/bin/env python

import paramiko
from getpass import getpass
import time

#ip = raw_input("Please enter your IP address: ")
username = raw_input("Please enter your username: ")
password = getpass()

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

timestamp = time.strftime("%d" + "-" + "%m" + "-" + "%Y")

f=open("loopbacks")

for line in f:
    try:
        print "Se acceseaza hostul: " + line 
        HOST=line.strip()
#        remote_conn_pre=paramiko.SSHClient()
#        remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        remote_conn_pre.connect(HOST, port=22, username=username,
                                password=password,
                                look_for_keys=False, allow_agent=False)


        remote_conn = remote_conn_pre.invoke_shell()
        remote_conn.send("terminal length 0\n")
        time.sleep(.5)

        remote_conn.send("show run\n")
        time.sleep(.5)

        remote_conn.send("exit\n")
        time.sleep(.5)

        readoutput = remote_conn.recv(65535)
	saveoutput=open("config_host_" + HOST + "_" + timestamp, "w")
	saveoutput.write(readoutput)
        saveoutput.close        
#	print readoutput

    except:
        print("Hostul " + str(HOST) + " e down.")
