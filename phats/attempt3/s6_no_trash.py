# Karina
# https://www.csnewbs.com/python-10c-remove-edit-lines

with open("output/3043210_s5_find_replace.txt", "r") as file:
    lines = file.readlines()
with open('sourcefiles/3043210_siuksles.txt', 'r') as file:
    to_delete = file.read().splitlines()

file = open("output/3043210_s5_find_replace.txt", "w")
for line in lines:
    if line.rstrip() not in to_delete:
        file.write(line)
        # print(line, "liko po pravalymo")

file.close()

# Karina
