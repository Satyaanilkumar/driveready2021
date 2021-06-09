x,y,z,n=map(int,input().split())
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if (i+j+k)!=n:
               print([i,j,k])
