# double prize money weekend bonanza
prizes = [5, 10, 50, 100, 1000]

# regular way to make the prizes double

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

# COMPERHENSION method to make the prize double
# does the same job but in less lines of code

dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)



# SQUARING OF NUMBERS
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_nums = []
for num in nums:
    if(num  ** 2) % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)



# COMPREHENSION METHOD
# starting with what we want to output
# check maps.py for another example of comperhension
squared_even_nums = [num**2 for num in nums if(num**2)%2==0]
print(squared_even_nums)
