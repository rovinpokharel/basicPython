from __future__ import print_function
num = 17
test = 2
Prime = True
for test in range(2, num):
    if (num % test == 0 and num != test):
        print(num, "equal", test, "*",num/test)
        break
    #     Prime =False
    # if Prime:
    #     print(num,"is a prime number")
    # else:
    #     print(num,"is not a prime number")
else:
    print(num,"is a prime number")