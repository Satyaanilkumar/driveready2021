def amstrg(a):
    z,val2,temp,temp1,c=1,0,a,a,0
    while temp:
        temp=temp//10
        c =c + 1
    while a:
        z = a%10
        a = a//10
        val=1
        for i in range(c):
            val = val*z
        val2 =val2+ val
    if (temp1 == val2):
        return "Yes"
    else:
        return "No"
x,y=map(int,input("enter range from to : ").split())
Count=0
for i in range(x,y+1):
    if amstrg(i)=="Yes":
        print(i,",",end="")
        Count+=1;
print(end="\n")
print("The range of ",x," to ", y,": ", Count,end="\n")
