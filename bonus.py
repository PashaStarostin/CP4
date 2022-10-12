a = [int(x) for x in input().split()]
delta = int(input())
n = len(a)
minim = 1111111111111111111111

for i in range(n):
    if a[i] < minim:
        minim = a[i]

c = 0
for i in range(n):
    if a[i] - delta == minim:
        c += 1

print(c)
