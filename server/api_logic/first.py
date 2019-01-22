import os
import csv

def read_tsv(): 
	cwd = os.getcwd()
	print(cwd)
	with open(f'{cwd}/data/log.txt', 'r', encoding=None) as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		for row in tsvin:
			print(row)

read_tsv()