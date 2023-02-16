a = []
n = int(input())#string
m = int(input())#column

for i in range(n):
    b = []
    for j in range(m):
        b.append(int(input()))
    a.append(b)
for i in a:
    print(i)
