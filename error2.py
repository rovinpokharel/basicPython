from __future__ import print_function
while True:
    try:
        print("Let us solve the equation(x/2}/(x-y)")
        x = float(input("Please enter a value of x:"))
        y = float(input("Please enter a value of y:"))
        if x == 0 or y == 0:
            break
        z = (x/2)/(x-y)
        print("Solving (x/2)/(x-y) for value x =",x,"and y",y,"we will get the result:",z)
    except Exception as e:
        print("There was an error with the code")
        print("Error message:",str(e))