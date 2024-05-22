import os
from tkinter import filedialog
import sys

def rename_files(files, old_substring, new_substring):
	"""
	Renames selected files by replacing the old substring with the new substring.
	
	Parameters:
	- files: list of files to be renamed (full paths)
	- old_substring: substring to be replaced in the filenames
	- new_substring: substring to replace the old substring
	"""
	try:
		for file in files:
			old_file_path = file
			directory, filename = os.path.split(file)
			# Replace the old substring with the new substring
			new_filename = filename.replace(old_substring, new_substring)
			new_file_path = os.path.join(directory, new_filename)
			
			# Rename the file
			os.rename(old_file_path, new_file_path)
			print(f'Renamed: {old_file_path} to {new_file_path}')
	
	except Exception as e:
		print(f'Error: {e}')

if __name__ == "__main__":
	selected_files = filedialog.askopenfilenames(title="Select files", initialdir=os.getcwd(), multiple=True)
	if not selected_files:
		print("No files selected.")
		sys.exit()

	old_string = 'ogfx'
	new_string = 'type2'

	rename_files(selected_files, old_string, new_string)
