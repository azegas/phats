file = open("sourcefiles/practice.txt", "r")
lines = file.readlines()
file.close()

siuksle = input("enter a trash to remove from the list: ")

file = open("sourcefiles/practice.txt", "w")
for line in lines:
    if line.rstrip()!= siuksle:
        file.write(line)

print(siuksle, "has been removed!")

file.close()


# open("sourcefiles/3043210_siuksles.txt", "r")





# issiunciau sita

# with open("sourcefiles/practice.txt", "r") as f:
#     lines = f.readlines()

# with open("sourcefiles/3043210_siuksles.txt", "r") as f:
#     siuksles = f.readlines()

# def remove_all_trash(sarasas, trashs):
#     for trash in trashs:
#         while trash in sarasas:
#             lines.remove(trash)

            
# remove_all_trash(lines, siuksles)

# issiunciau sita


# # Write-Overwrites
# file1 = open("sourcefiles/practice.txt","w")
# file1.write(blet)
# file1.close()

            
# for line in lines:
#     if siuksle in siuksles:
#         lines.remove(siuksle)
        



        
# with open("sourcefiles/practice.txt", "w") as f:
#     trash = ['3003610_P--', '3048490_P-3', '2971611_P-2']

# def remove_all_trash(list_obj, values):
#     for value in values:
#         while value in list_obj:
#             source.remove(value)
#     print('removed the trash')
