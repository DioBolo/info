n = int(input())
t = [0]*(n+1)
c = 0
for i in range(1,n+1):
    x,y = [int(j) for j in input().split()]
    t[i] = t[i-1]+(y-x)
for k in range(n):
    if t[k]>t[k-1]:
        c=k+1
    #elif t[k]<t[k-1]:
        #c=0

print(c)
