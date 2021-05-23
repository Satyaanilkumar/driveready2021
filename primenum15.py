import math as m
def prime1(num):
    if num==1:
        return False
    if num== 2 or num==3 or num==5 or num==7:
        return True
    return False
def megaprime1(num,z):
    temp,c=num,0
    while temp:
        c += 1
        temp = temp // 10
    while num:
        r=num%10
        if num<=10:
            x=prime1(r)
            if x==True:
                return True
            return False
        if (num%2==0) or (num%3==0) or (num%5==0) or (num%7==0):
            return False
        else:
            for i in range (c):
                x=prime1(r)
                if x==True:
                    return True

            return False
        num = num // 10



a=int(input())
z=int(m.sqrt(a))
print(megaprime1(a,z))
