n = int(input())
o = 0
c = 0
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if i == 0:
        o = y
    else:
        if o-x <= 0:
            c+=1
        o+=y-x
print(c)