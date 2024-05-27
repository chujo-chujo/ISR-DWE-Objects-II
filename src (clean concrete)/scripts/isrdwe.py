import sys
import os
from datetime import datetime
from header import *
from lists_of_objects import *
from templates import *
from templates2 import *

############################################################################
# HELPER FUNCTIONS

def replace_keywords(dict_of_object, template):
	""" Create nml code by replacing keywords in a given template """
	for key, value in dict_of_object.items():
		template = template.replace(key, str(value))
	return template

def number_objects(NML):
	""" Replace 'NUMERO' with three-digit numbers """
	result = []
	for counter, item in enumerate(NML, start=0):			# "start" is shifted, first appended NML is header.py
		item = item.replace("NUMERO", f"{counter:03d}")
		result.append(item)
	return result

def update_lang_file():
	""" Add the current date to the lang file """
	# Get current date, format the date as "Month day, year"
	current_datetime = datetime.now()
	formatted_date = "{LTBLUE}" + current_datetime.strftime("%B %d, %Y")
	
	# Open lang file, replace old date with new one
	with open("lang/english.lng", 'r') as file:
		english_lng = file.readlines()
	
	english_lng_with_date = []
	for line in english_lng:
		index = line.find("{LTBLUE}")
		if index != -1:
			line = line[:index] + formatted_date + "\n"
		english_lng_with_date.append(line)
	
	with open("lang/english.lng", 'w') as file:
		file.write("".join(english_lng_with_date))

############################################################################
# GENERATE CODE, INSERT OBJECTS INTO TEMPLATES, GIVE NUMBER TO EACH OBJECT, ADD DATE TO .LANG:

NML = []

NML.append(header)

for n in list_of_Normal_ISR_DWE_tiles:
	replaced = replace_keywords(n, template_4obj)
	NML.append(replaced)

for n in list_of_Transition_tiles:
	replaced = replace_keywords(n, template_Transition_tiles)
	NML.append(replaced)

for n in list_of_ISR_DWE_roads:
	replaced = replace_keywords(n, template_4obj)
	NML.append(replaced)

for n in list_of_Fixtures:
	replaced = replace_keywords(n, template_4obj_cc)
	NML.append(replaced)

for n in list_of_Vehicles:
	replaced = replace_keywords(n, template_4obj_cc)
	NML.append(replaced)

for n in list_of_Road_overlapping_tiles:
	replaced = replace_keywords(n, template_Dock_overlapping_tiles_cc)
	NML.append(replaced)

for n in list_of_Drive_through_tiles:
	replaced = replace_keywords(n, template_Dock_overlapping_tiles_cc)
	NML.append(replaced)

for n in list_of_Dock_overlapping_tiles:
	replaced = replace_keywords(n, template_Dock_overlapping_tiles)
	NML.append(replaced)

for n in list_of_Dock_overlapping_tiles_water:
	replaced = replace_keywords(n, template_Dock_overlapping_tiles_water)
	NML.append(replaced)

for n in list_of_Water_based_tiles:
	replaced = replace_keywords(n, template_Water_based_tiles)
	NML.append(replaced)

for n in list_of_Cargo_tiles_random:
	if len(n) < 45:
		replaced = replace_keywords(n, template_Cargo_1obj_random)
	else:
		replaced = replace_keywords(n, template_Cargo_4obj_random)
	NML.append(replaced)

for n in list_of_Cargo_tiles:
	replaced = replace_keywords(n, template_4obj)
	NML.append(replaced)

for n in list_of_Ships:
	replaced = replace_keywords(n, template_Ships)
	NML.append(replaced)

# dev info
print(f"Number of Normal_ISR_DWE_tiles: {len(list_of_Normal_ISR_DWE_tiles) + len(list_of_Transition_tiles)}")
print(f"Number of ISR_DWE_roads: {len(list_of_ISR_DWE_roads)}")
print(f"Number of Fixtures: {len(list_of_Fixtures)}")
print(f"Number of Vehicles: {len(list_of_Vehicles)}")
print(f"Number of Road_overlapping_tiles: {len(list_of_Road_overlapping_tiles)}")
print(f"Number of Drive_through_tiles: {len(list_of_Drive_through_tiles)}")
print(f"Number of Water_based_tiles: {len(list_of_Water_based_tiles)}")
print(f"Number of Dock_overlapping_tiles: {len(list_of_Dock_overlapping_tiles) + len(list_of_Dock_overlapping_tiles_water)}")
print(f"Number of Cargo_tiles: {len(list_of_Cargo_tiles_random) + len(list_of_Cargo_tiles)}")
print(f"Number of Ships: {len(list_of_Ships)}")
print(f"------------------------------------------")
print(f"Total: {len(NML)}")
print(f"------------------------------------------")
print(f"Number of lines of code: {sum(len(s.splitlines()) for s in NML)}")


# Number all objects, replace 'NUMERO' with a number
NML = number_objects(NML)

# Add current date to the language file
update_lang_file()


# Write the list of NML strings into a file
file_path = "isrdwe_objects_clean.nml"

if os.path.exists(file_path):
  os.remove(file_path)

with open(file_path, 'w') as file:
	file.write("\n".join(NML))


