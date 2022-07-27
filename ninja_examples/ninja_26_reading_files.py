ipsum_file = open('files/ipsum.txt')

# USING FOR LOOP METHOD
for line in ipsum_file:
    print(line.rstrip())        # rstrip - removes blank lines only

# USING READLINES METHOD. need to get the cursor back at the start again

ipsum_file.seek(0)              # cursor back to the start

lines = ipsum_file.readlines()  # comma separated list
print(lines)

# ONE MORE METHOD

ipsum_file.seek(50)             # read FROM 50 char
file_text = ipsum_file.read(100)  # read only 100 chars
print(file_text)

ipsum_file.close()              # IMPORTANT TO CLOSE FILE FOR PERFORMANCE


# A way that doesn't require us to close the file after the operation
