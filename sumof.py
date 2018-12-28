from __future__ import print_function
x = [1,2,5,8,9,6]
evenSum = 0
oddSum = 0
for n in x:
    if n % 2 == 0:
        evenSum = evenSum + n
    else:
        oddSum = oddSum + n
print("number provided", x)
print("Sum of even number is", evenSum)
print("Sum of odd number is", oddSum)

