#!/usr/bin/env python

import ipaddress
import csv

ipadd = raw_input('Introduceti adresa (A.B.C.D/nm): ')
host = ipaddress.ip_interface(unicode(ipadd))
net = host.network

print('-------------------------------------------------')
print('Masca de retea este: ' + str(host.netmask))
print('-------------------------------------------------')
print('Adresa de retea este: ' + str(net))
print('-------------------------------------------------')
print('Numarul de hosturi este: ' + str(net.num_addresses))
print('-------------------------------------------------')

y=str('y')
s=str('s')
n = ipaddress.ip_network(net)

answer1 = raw_input('Doriti sa  vedeti hosturile utilizabile ?\n (y/n, Save in silent mode: s)   ')

if answer1 == y:
	print("Lista hosturilor va fi salvata in fisierul hosts.csv")
	for ip in n.hosts():
		with open("hosts.csv", "a") as output1:
			writer1 = csv.writer(output1)
			writer1.writerow([ip,str(host.netmask)])
		print ip

elif answer1 == s:
	print("Lista hosturilor va fi salvata in fisierul hosts.csv")
        for ip in n.hosts():
                with open("hosts.csv", "a") as output1:
                        writer1 = csv.writer(output1)
                        writer1.writerow([ip,str(host.netmask)])

else:
	print('OK, moving on.')

print('-------------------------------------------------')

answer2 = raw_input('Doriti sa subnetizati ?\n (y/n, Save in silent mode: s)   ')

if answer2 == y:
	newcidr = raw_input('introduceti noul CIRD: ')
	print('Lista subneturilor va fi salvata in fisierul subnets.csv')
	for nets in n.subnets(new_prefix=int(newcidr)):
		with open("subnets.csv", "a") as output2:
                        writer2 = csv.writer(output2)
			writer2.writerow([nets,])
#                        writer2.writerow([nets, "/"+str(newcidr)])
		print nets

elif answer2 == s:
	newcidr = raw_input('introduceti noul CIRD: ')
        print('Lista subneturilor va fi salvata in fisierul subnets.csv')
        for nets in n.subnets(new_prefix=int(newcidr)):
                with open("subnets.csv", "a") as output2:
                        writer2 = csv.writer(output2)
                        writer2.writerow([nets,])

else:
	print("That's all for now. Bye!")
