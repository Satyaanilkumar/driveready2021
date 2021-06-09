def rotv(ilist,index):
    if index<=(len(ilist)-1):
        for i in range(index):
            anil=ilist[0]
            ilist.pop(0)
            ilist.append(anil)
        print(ilist)
    else:
        print("index error")
Ilist=list(input("enter: ").split())
ind=int(input("Rotate NUmber: "))
rotv(Ilist,ind)
