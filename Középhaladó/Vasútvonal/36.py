n = int(input())
e = 0
q = -1
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if i == 0:
        e = y
    else:
        if y > e and y != 0 and e != 0 and q == -1:
            q = i+1
    e = y
print(q)