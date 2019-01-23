import os
import csv

def read_tsv(): 
	cwd = os.getcwd()
	print(cwd)
	with open(f'{cwd}/data/log.txt', 'r', encoding=None) as tsvin:
		tsvin = csv.reader(tsvin, delimiter='\t')
		log_list = []
		log_dic = {}
		for row in tsvin:
			log_dic = {
				'auto_type': row[0],
				'cart_number': row[1],
				'title': row[2],
				'length': row[3],
				'temp':row[4],
				'month': row[5],
				'day': row[6],
				'year': row[7],
				'hour': row[8]
			}
			log_list.append(log_dic)
		return log_list


# read_tsv()