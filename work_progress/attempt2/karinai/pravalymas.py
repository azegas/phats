# attempt 2
# https://www.csnewbs.com/python-10c-remove-edit-lines

file = open("source.txt", "r")
lines = file.readlines()
file.close()

fruit = input("enter a trash to remove from the list: ")

file = open("source.txt", "w")
for line in lines:
    if line.rstrip() != fruit:
        file.write(line)

print(fruit, "has been removed!")

file.close()

# attempt 1

# with open("practice.txt", "r") as f:
#     lines = f.readlines()

# with open("3043210_siuksles.txt", "r") as f:
#     siuksles = f.readlines()

# def remove_all_trash(sarasas, trashs):
#     for trash in trashs:
#         while trash in sarasas:
#             lines.remove(trash)

            
# remove_all_trash(lines, siuksles)
