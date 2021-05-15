n1,n2=map(int,input().split())
t=2
c=1
while True:
    if n1%t==0 and n2%t==0:
        n1=n1/t
        n2=n2/t
        c=c*t
    elif t>=n1 or t>=n2:
        c=c*n1*n2
        break

    else:
        t = t + 1
print(c)