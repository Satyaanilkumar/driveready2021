num=int(input())
d=num%10
num = num//10
while num:
    r=num%10
    num=num//10
    if (d%2==0 and r%2==0) or (d%2==1 and r%2==1):
        print("not in a form")
        break
    d=r
else:
    print("wave form")