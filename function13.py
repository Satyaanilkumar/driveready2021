
def perfect(a):
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=i
    if a==c:
        return "Yes"
    elif a!=c:
        return "No"
a,b=map(int,input("Enter Range from and to: ").split())
c=0
for i in range (a,b+1):
    if perfect(i)=="Yes":
        c+=1
        print(i,",",end="")
print(end="\n")
print("perfect numbers between",a,"&",b," : ", c)

