import os
import csv

def read_tsv(): 
	cwd = os.getcwd()
	print(cwd)
	with open(f'{cwd}/data/log.txt', 'r', encoding=None) as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		log_list = []
		for row in tsvin:
			log_list.append(row)
		return log_list


# read_tsv()