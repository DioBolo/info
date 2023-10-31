n = int(input())
l = [0,2,5]
for i in range(3, n+1):
    l.append(2*l[-1]+l[-2])

print(l[n]%20201114)
