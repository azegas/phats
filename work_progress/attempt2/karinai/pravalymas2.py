# attempt 2
# https://www.csnewbs.com/python-10c-remove-edit-lines

with open("source.txt", "r") as file:
    lines = file.readlines()
with open('siuksles.txt', 'r') as file:
    to_delete = file.read().splitlines()

file = open("source.txt", "w")
for line in lines:
    if line.rstrip() not in to_delete:
        file.write(line)
        print(line, "liko po pravalymo")

file.close()
