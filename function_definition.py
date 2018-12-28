def exp(x,y):
    z = x ** y
    print(z)

def add(a,b):
    s = a + b
    print(s)

def printFib(n):
    a,b = 0,1
    while b < n:
        print(b)
        a,b = b,a+b

def calFib(n):
    result = []
    a,b = 0,1
    while b<n:
        result.append(b)
        a,b = b, a+b
    return result
