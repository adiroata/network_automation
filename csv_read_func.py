import csv

def get_cell(col, row):
	with open ('database.csv', 'r') as csv_file:
		reader = csv.reader(csv_file)
		row_read = 0

		for line in reader:
			if row_read == row:
				cell = line[col]
				return cell
			row_read +=1

cell_x = get_cell(0, 0)


print(cell_x)
