#!/usr/bin/env python
import csv
import easysnmp

def get_cell(col, row):
    with open('database.csv') as f:
        reader = csv.reader(f)
        row_count = 0
        for n in reader:
            if row_count == row:
                cell = n[col]
                return cell
            row_count += 1


for n in range(4):
	HOST = get_cell(0, n)

	session = easysnmp.Session(hostname=str(HOST), community='public', version=2)
	sys_walk = session.walk('.1.3.6.1.2.1.4.20.1.2')

	for item in sys_walk:
		sys_id=session.get('.1.3.6.1.2.1.1.5.0')
		sys_ipaddr=item.oid_index
		index=item.value
		sys_if = session.get('.1.3.6.1.2.1.2.2.1.2.' + index)
		sys_if_desc = session.get('.1.3.6.1.2.1.31.1.1.1.18.' + index)
		print(str(sys_id.value) + ' | ' + str(sys_if.value) + ' | ' + str(sys_if_desc.value)  + ' | ' + str(sys_ipaddr))

		
