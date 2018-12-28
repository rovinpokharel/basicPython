from __future__ import print_function
def abs(x):
    if x<0:
        x=x*-1
        return x
    else:
        return x

int = int(input("Enter a number: "))
print(abs(int))