n = int(input())
l = 0
f = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    l += x
    f += y

if f == l:
    print(1)
else:
    print(0)
