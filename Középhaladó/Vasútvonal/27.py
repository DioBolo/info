n = int(input())
m = int(input())
p = [0]
for i in range(n):
    x,y = [int(j) for j in input().split()]
    p.append(p[-1]+(y-x))

print(sum(p)*m)