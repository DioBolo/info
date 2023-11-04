n = int(input())
c = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    c+=y

print(c)
