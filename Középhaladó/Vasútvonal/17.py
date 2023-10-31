n,m = [int(i) for i in input().split()]
l = [0]
q = [0,0]
a = [[0,0]]
b = []
for i in range(1,n+1):
    x,y = [int(j) for j in input().split()]
    l.append(l[i-1]+y-x)


#if l.count(m) >= 1:
#    h = l.index(m)
#    q[0] = h
#    while l[h] == m:
#        h += 1
#    q[1] = h

for c in l:
    if c >= m:
        h = l.index(c)
        q[0] = h
        while l[h] >= m:
            h += 1
        q[1] = h
        if max(a)[-1] != q[1]:
            a.append([q[0],q[1]])
            b.append(c)

print(l)
#print(l.count(m))
print(a)

#if l.count(m) >= 1:
#    h = l.index(m)
#    q[0] = h
#    while l[h] == m:
#        h += 1
#    q[1] = h

# for c in l:
#     if c >= m:
#         h = l.index(c)
#         q[0] = h
#         while l[h] >= m:
#             h += 1
#         q[1] = h
#         if max(a)[-1] != q[1]:
#             a.append([q[0],q[1]])
#             b.append(c)