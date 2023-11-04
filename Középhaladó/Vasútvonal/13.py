n = int(input())
c = 1024
q = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if x < c and x!=0:
        c = x
        q = i+1

print(q)
        
