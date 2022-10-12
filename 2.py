a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

c = []

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c.append(a[i])

print(*set(c))