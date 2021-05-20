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
        print("it is a amstrong number", temp1)
    else:
        print("it is not a amstrong number", temp1 )
a=int(input("enter : "))
amstrg(a)