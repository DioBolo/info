n = int(input())
l = [0]
for i in range(n):
    x,y = [int(j) for j in input().split()]
    l.append(l[-1]+(y-x))
l.pop(0)
print(*l)