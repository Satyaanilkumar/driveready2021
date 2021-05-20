
def perfect(a):
    c=0
    for i in range(1,a):
        if a%i==0:
            c+=i
    if a==c:
            print("perfect Number")
    elif a!=c:
        print("Not a Perfect Number")
a=int(input("Enter: "))
perfect(a)