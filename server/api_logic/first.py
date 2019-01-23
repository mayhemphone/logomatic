import os
import csv

def read_tsv(): 
	cwd = os.getcwd()
	print(cwd)
	with open(f'{cwd}/data/shortlog.txt', 'r', encoding=None) as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		for row in tsvin:
			 # print(row)
			 rowstuff = row
			 rowstuff = [row.replace('410607','999999') for row in rowstuff]
			 print(rowstuff)
	# print(type(rowstuff))

read_tsv()
