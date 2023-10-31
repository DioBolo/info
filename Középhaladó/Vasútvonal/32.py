n = int(input())
o = [0]
for i in range(n):
    x,y = [int(j) for j in input().split()]
    o.append(o[-1]+(y-x))

q = 1
while o[q] == 0:
    q += 1
print(q)