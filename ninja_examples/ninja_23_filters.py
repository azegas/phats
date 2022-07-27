#############################################
# # TASK - remove all F's from your grades. #
#############################################

grades = ['A', 'B', 'F', 'C', 'F', 'A']


# USING a FILTER

def remove_fails(grade):
    return grade != 'F'         # not equal to F


print(filter(remove_fails, grades))  # getting this output <filter object at 0x7f30487caa90>

# BUT if we add 'list' idk?, then it works

print(list(filter(remove_fails, grades)))

######################
# # USING A FOR LOOP #
######################

filtered_grades = []

for ick in grades:
    if ick != 'F':
        filtered_grades.append(ick)

print(filtered_grades)


#######################
# Using comperhension #
#######################

print([grade for grade in grades if grade != 'F'])
