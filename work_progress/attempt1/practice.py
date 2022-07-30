def remove_all_by_values(list_obj, values):
    for value in values:
        while value in list_obj:
            list_of_num.remove(value)


list_of_num = [51, 52, 52, 55, 55, 52, 57, 52, 55, 61, 62]

remove_all_by_values(list_of_num, [52, 55, 57])
print(list_of_num)


with open("sourcefiles/practice.txt", "r") as f:
    lines = f.readlines()
with open("sourcefiles/practice.txt", "w") as f:
    for line in lines:
        if line.strip("\n") != "3003610_P--":
            f.write(line)
