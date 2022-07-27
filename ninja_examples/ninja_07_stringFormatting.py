
"""
This and that important stuff.

Bela.
"""


num1 = 3.14256546456
num2 = 10.534677467

# PREVIOUS WAY
print('num1 is', num1, 'and num2 is', num2)


# FORMAT METHOD
# nice, store the values and then use indexes to take them
print('num1 is {0} and num 2 is {1}'.format(num1, num2))

# apply some PRECISION for the numbers. So useful for my fbdjango
# script!! Show only 3 numbers.
print('num1 is {0:.3} and num 2 is {1:.5}'.format(num1, num2))

# 3 decimal points only.
print('num1 is {0:.3f} and num 2 is {1:.5f}'.format(num1, num2))


# GUY's FAVORITE WAY
# using F-STRING

print(f'num1 is {num1:.3f} and num2 is {num2}')
