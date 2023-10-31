n = int(input())
c = -1
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if x+y == 0 and i != 0 and i!= n-1 and c == -1:
        c = i+1

print(c)