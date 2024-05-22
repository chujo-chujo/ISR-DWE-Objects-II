import os
from tkinter import filedialog
import sys

def add_incrementing_numbers(filename, keyword):
	try:
		with open(filename, 'r') as file:
			lines = file.readlines()

		counter = 1
		with open(filename[:-4]+"_numbered.txt", 'w') as file:
			for line in lines:
				if keyword in line:
					line = line.replace(keyword, f'{keyword}_{counter:02d}')
					counter += 1
				file.write(line)
				
		print(f"Keyword '{keyword}' has been numbered {counter-1} times.")

	except FileNotFoundError:
		print(f"The file '{filename}' does not exist.")

####################################################

filename = filedialog.askopenfilename(initialdir=os.getcwd())
if not filename:
	sys.exit()

keyword = '"Road_overlapping_tiles'

add_incrementing_numbers(filename, keyword)
