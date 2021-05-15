num=int(input())
e=num%2==0;
o=num%2==1;
while num:
    r=num%10;
    num=num//10
    if e and r%2==1:
        print("even odd")
        break
    if o and r%2==0:
        print("odd even")
        break
else:
    if e:
        print("even")
    if o:
        print("odd")