def find_first_difference(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        line_num = 1
        for line1, line2 in zip(f1, f2):
            if line1 != line2:
                return line_num
            line_num += 1
        # Check if one file has more lines than the other
        if any(f1) or any(f2):
            return line_num
    return None


file1 = '4obj.txt'
file2 = 'dock.txt'
difference_line = find_first_difference(file1, file2)
if difference_line:
    print(f"The first different line is at line {difference_line}")
else:
    print("The files are identical")
