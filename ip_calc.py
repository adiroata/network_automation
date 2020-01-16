#!/usr/bin/env python

import ipaddress
import os
import csv

ipadd = raw_input('Introduceti adresa (A.B.C.D/nm): ')
host = ipaddress.ip_interface(unicode(ipadd))
hostonly=host.ip
net = host.network

print('-------------------------------------------------\n')
print('Adresa de retea este: ' + str(net))
print('-------------------------------------------------\n')
print('Adresa reverse DNS este: ' + str(hostonly.reverse_pointer))
print('-------------------------------------------------\n')
print('Masca de retea este: ' + str(host.netmask))
print('-------------------------------------------------\n')
print('Wildcard mask este: ' + str(host.hostmask))
print('-------------------------------------------------\n')
print('Numarul de hosturi este: ' + str(net.num_addresses))
print('-------------------------------------------------\n')

p=str('p')
ps=str('ps')
s=str('s')

n = ipaddress.ip_network(net)

answer1 = raw_input('List hosts ?\n\nJust print: p\nPrint&Save: ps\nJust save: s\nAbort: a\n\nYour choice:   ')

if answer1 == p:
	for ip in n.hosts():
		print ip

elif answer1 == ps:
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

print('-------------------------------------------------\n')

answer2 = raw_input('List subnets ?\n\nJust print: p\nPrint&Save: ps\nJust save: s\nAbort: a\n\nYour choice:   ')

if answer2 == p:
        newcidr = raw_input('introduceti noul CIRD: ')
        for nets in n.subnets(new_prefix=int(newcidr)):
                print nets

elif answer2 == ps:
	newcidr = raw_input('introduceti noul CIRD: ')
	print('Lista subneturilor va fi salvata in fisierul subnets.csv')
	for nets in n.subnets(new_prefix=int(newcidr)):
		with open("subnets.csv", "a") as output2:
                        writer2 = csv.writer(output2)
			writer2.writerow([nets,])
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

# Writen by Adrian Roata | adi.roata@gmail.com
