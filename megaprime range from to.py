import math as m
def prime1(num,z):
    if num==1:
        return False
    if num<10:
        if (num==2) or (num==3) or (num==5) or (num==7) or (num % z != 0):
            return True
        return False
    elif (num%2==0) or (num%3==0) or (num%5==0) or (num%7==0)  or (num%z==0):
        return False
    return True
def megaprime1(num,z):
    temp,temp1,c=num,num,0
    while temp:
        c+=1
        temp=temp//10
    ch1 = True
    ch2 = True
    while num:
        r = num % 10
        num = num // 10

        checkd=prime1(temp1,z)
        if checkd==False:
            ch2=False
        if checkd==True:
            ch=prime1(r,1)
            if ch==False:
                 ch1=False
    if (ch1 == False) or (ch2==False):
        return False
    if (ch2==True) and (ch1== True):
        return True
a,b=map(int,input("enter: ").split())
# z=int(m.sqrt(a))
# print(megaprime1(a,z))
c=0
for i in range (a,b+1):
    z = int(m.sqrt(i))
    if megaprime1(i,z)== True:
        print(i,",",end="")
        c+=1
print("\n")
print("the mega prime numbers between " ,a,"to ",b,"=", c)



