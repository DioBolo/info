n = int(input())
c = 1024
q = 0
for i in range(1,n+1):
    x,y = [int(j) for j in input().split()]
    if x > y and x-y<c:
        c = x-y
        q = i
print(q)

        
