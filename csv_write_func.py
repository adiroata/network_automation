import csv

def write_cell(row, col, new_value):
	with open('testdb.csv', 'r') as csv_file_old:
		reader = csv.reader(csv_file_old)
		my_value = list(reader)
		csv_file_old.close()

		my_value[row][col] = new_value

		with open('testdb.csv','w') as csv_file_new:
			writer = csv.writer(csv_file_new)
			writer.writerows(my_value)
			csv_file_new.close()
		return ""

print('Introduceti: Rand, Coloana, Valoare')
new = write_cell(int(raw_input()), int(raw_input()), raw_input())

print(new)
