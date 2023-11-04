n = int(input())
c = 0
q = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if (c+y)-x < c:
        c = (c+y)-x
        q+=1

print(q)
