n = int(input())
c = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if x != 0 and y != 0:
        c += 1
print(c)