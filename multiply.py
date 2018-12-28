from __future__ import print_function
num = 12
for x in range(1,11):
    print(x,"x",num,"=",x*num)

def multable(x,y):
    for i in range(1,y+1):
        for j in range(1,x+1):
            print( i*j,"\t", end ="")
        print("\n")
multable(5,7)
