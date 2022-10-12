a = [float(x) for x in input().split()]
n = len(a)
maxim = -1111111111
for i in range(n):
    if a[i] > maxim:
        maxim = a[i]

k = 0
for i in range(n):
    if a[i] == maxim and k == 0:
        k = 1
    elif k == 1:
        a[i] = 0

print(a)