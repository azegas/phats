with open("sourcefiles/practice.txt", "r") as f:
    source = f.readlines()
with open("sourcefiles/practice.txt", "w") as f:

print(source_contents)

# a = open('sourcefiles/3043210siukslesClean.txt','r')
trash = ['3003610_P--', '3048490_P-3', '2971611_P-2']

def remove_all_trash(list_obj, values):
    for value in values:
        while value in list_obj:
            source.remove(value)
    print('removed the trash')
    
remove_all_trash(source, trash)
print(source_contents)
