n = int(input())
c = 1024
q = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if y < c and i!=n-1:
        c = y
        q = i+1

print(q)
        
