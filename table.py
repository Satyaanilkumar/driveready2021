num,key=map(int,input().split())
while num:
    r=num%10
    num=num//10
    if r==key:
        print("found")
        break
else:
    print("not found")