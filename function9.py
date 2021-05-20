def sam(a,b):
    while True:
        if a==1:
            return b
        if a>1:
            return sam(a//2,b*2)
a,b=map(int,input().split())
print(sam(a,b))