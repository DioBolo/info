n = int(input())
c = 1024
q = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if x+y<c:
        c = x+y
        q = i+1

print(q)
        
