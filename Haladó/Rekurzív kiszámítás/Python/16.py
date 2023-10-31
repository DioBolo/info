n = int(input())
l = [0,2,4,9]
for i in range(4,n+1):
    l.append(2*l[-1]+l[-3])

print(l[n]%20201114)
