import math

num = input("enter the number: ")
temp = set()
output = []
for i in range(0, len(num)):
    for j in range(i, len(num)):

        substr = int(num[i:j + 1])
        temp.add(substr)
temp = sorted(list(temp))
print("substrings: ", temp)
for num1 in temp:
    val = int(math.sqrt(num1));
    if (val * (val + 1) == num1):
        output.append(num1)

print(output)
