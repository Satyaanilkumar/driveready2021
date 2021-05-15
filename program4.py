a,b=map(int,input().split())
num=0
count=0
v=1
while a:
    a=(a//2)
    b=b*2

    if a%2==1:
        count=count+b

print(count)

