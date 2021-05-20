def lcm(x,y):
    t=2
    res=1
    while True:
        if x%t==0 and y%t==0:
            x=x/t
            y=y/t
            res=res*t

        elif t>=x or t>=y:
            res = res * x*y
            break
        else:
            t+=1
    return res

a,b=map(int,input().split())
print(lcm(a,b))
