n = int(input())
lis = list(map(int, input().split()))
lis.sort()
lis.reverse()
l = len(lis)
t = max(lis)
for i in range(0, l, 1):
    if lis[i] != t:
        print(lis[i])
        break