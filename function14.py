import math as m
def ma(a):
    c = 0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
            print(i,",",end=" ")
    print("\n")
    print(c,"\n")
a=int(input("enter: "))
ma(a)