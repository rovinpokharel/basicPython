import math
def slope(m,x,c):
    y = m * x + c
    return y

m = int(input("Enter the value of slope(m): "))
x = int(input("Enter the value of x-intercept(X)"))
c = int(input("Enter the value of y-intercept(c)"))
print(slope(m,x,c))