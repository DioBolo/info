n = int(input())
o = 0
c = 0
v = False
for i in range(n):
    x,y = [int(j) for j in input().split()]
    if i == 0:
        o = y
    else:
        if o == o+(y-x) and not v:
            c = i+1
            v = True
        o+=y-x

if not v:
    print(n+1)
else:
    print(c)