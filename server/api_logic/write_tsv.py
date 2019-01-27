from read_txt import *
import csv
import os

log_list = read_tsv()

# print(log_list)

# TODO
# replace cart_number with number from a stored list somewhere else. Start with a hard coded list
# figure out where/how to store new file. will have to take use input and interpolate in path


# -----FAUX DB------
# log_list = [
# 	{'auto_type': '3', 'cart_number': 'change', 'title': 'NOTHING BREAKS LIKE A HE', 'length': '210', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '9', 'cart_number': '1', 'title': '*** DROP SONG ***', 'length': '0', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '4', 'cart_number': '566700', 'title': 'STABS 1061 - JOSH', 'length': '2', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '3', 'cart_number': '408817', 'title': 'GIRLS LIKE YOU', 'length': '234', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '4', 'cart_number': 'change', 'title': 'INTO STOPSET', 'length': '7', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '8', 'cart_number': '', 'title': '8 MIN Spotset', 'length': '', 'temp': '4', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}, 
# 	{'auto_type': '4', 'cart_number': '566600', 'title': 'KBKS LEGAL', 'length': '10', 'temp': '3', 'month': '1', 'day': '25', 'year': '19', 'hour': '23'}
# 	]

user_cart_numbers = ["1234000", "5678000", "17584000", "98723000", "92837000"]

# ------------------

for item in log_list:
	if item['cart_number'] == "change":
		item['cart_number'] = user_cart_numbers.pop(0)
# print(log_list)

f_log_list = []

for record in log_list:
	f_auto_type = record['auto_type'].ljust(2, ' ') 
	f_cart_number = record['cart_number'].ljust(8, ' ')
	f_title = record['title'].ljust(24, ' ')
	f_length = record['length'].ljust(4, ' ')
	f_temp = record['temp'].ljust(1, ' ')
	f_month = record['month'].ljust(3, ' ')
	f_day = record['day'].ljust(3, ' ')
	f_year = record['year'].ljust(2, ' ')
	f_hour = record['hour'].ljust(1, ' ')
	f_log_list.append([f_auto_type, f_cart_number, f_title, f_length, f_temp, f_month, f_day, f_year, f_hour])

print(len(f_log_list))

cwd = os.getcwd()
with open(f'{cwd}/data/output.txt', 'wt') as out_file:
	tsv_writer = csv.writer(out_file, delimiter=' ', quoting=csv.QUOTE_NONE, escapechar='None', quotechar='')
	for element in f_log_list:
		tsv_writer.writerow(element)
	print(type(tsv_writer))










