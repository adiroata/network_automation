#!/usr/bin/env python3

import ipaddress
import csv

ipadd = input('Introduceti adresa (A.B.C.D/nm): ')
host = ipaddress.ip_interface(ipadd)
hostonly=host.ip
net = host.network
hosts_number=int(net.num_addresses)-2

print('-------------------------------------------------\n')
print('Adresa de retea este: ' + str(net))
print('-------------------------------------------------\n')
print('Adresa reverse DNS este: ' + str(hostonly.reverse_pointer))
print('-------------------------------------------------\n')
print('Masca de retea este: ' + str(host.netmask))
print('-------------------------------------------------\n')
print('Wildcard mask este: ' + str(host.hostmask))
print('-------------------------------------------------\n')
#print('Numarul de hosturi este: ' + (int(net.num_addresses)-2))
print('Numarul de hosturi este: ' + str(hosts_number))
print('-------------------------------------------------\n')

p=str('p')
ps=str('ps')
s=str('s')

n = ipaddress.ip_network(net)

answer1 = input('List hosts ?\n\nJust print: p\nPrint&Save: ps\nJust save: s\nAbort: a\n\nYour choice:   ')

if answer1 == p:
    for ip in n.hosts():
        print (ip)

elif answer1 == ps:
    print("Lista hosturilor va fi salvata in fisierul hosts.csv")
    for ip in n.hosts():
        with open("hosts.csv", "a") as output1:
            writer1 = csv.writer(output1)
            writer1.writerow([ip,str(host.netmask)])
        print (ip)

elif answer1 == s:
    print("Lista hosturilor va fi salvata in fisierul hosts.csv")
    for ip in n.hosts():
        with open("hosts.csv", "a") as output1:
            writer1 = csv.writer(output1)
            writer1.writerow([ip,str(host.netmask)])

else:
    print('OK, moving on.')

print('-------------------------------------------------\n')

answer2 = input('List subnets ?\n\nJust print: p\nPrint&Save: ps\nJust save: s\nAbort: a\n\nYour choice:   ')

if answer2 == p:
    newcidr = input('introduceti noul CIDR: ')
    for nets in n.subnets(new_prefix=int(newcidr)):
        print (nets)

elif answer2 == ps:
    newcidr = input('introduceti noul CIDR: ')
    print('Lista subneturilor va fi salvata in fisierul subnets.csv')
    for nets in n.subnets(new_prefix=int(newcidr)):
        with open("subnets.csv", "a") as output2:
            writer2 = csv.writer(output2)
            writer2.writerow([nets,])
            print (nets)

elif answer2 == s:
    newcidr = input('introduceti noul CIDR: ')
    print('Lista subneturilor va fi salvata in fisierul subnets.csv')
    for nets in n.subnets(new_prefix=int(newcidr)):
        with open("subnets.csv", "a") as output2:
            writer2 = csv.writer(output2)
            writer2.writerow([nets,])

else:
    print("That's all for now. Bye!")

