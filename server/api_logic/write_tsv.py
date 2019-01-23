from read_txt import *
import csv
import os

log_list = read_tsv()

print(log_list[0])

# log_list[0] = [element.replace(log_list[0][0], '1600') for element in log_list[0]]
# altered_log = log_list[0].replace(log_list[0][0], 'new')
# index 1 is cart number
# log_list[0].cart_number = '1600'
log_list[0]['cart_number'] = 'poop'
cwd = os.getcwd()
with open(f'{cwd}/data/output.tsv', 'wt') as out_file:
	tsv_writer = csv.writer(out_file, delimiter='\t')
	tsv_writer.writerow(log_list[0])

print(log_list[0])