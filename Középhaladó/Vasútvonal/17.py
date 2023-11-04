def kulonb(l):
    return l[1] - l[0]

def main():
    n,m = [int(i) for i in input().split()]
    fl = [False]*(n+1)
    q = [0,0]
    a = [[0,0]]
    u = [0]
    e = 0
    for i in range(1,n+1):
        x,y = [int(j) for j in input().split()]
        e += y-x
        if e >= m:
            fl[i] = True

    c = 0
    for k in fl:
        if k:
            q[0] = c
            while fl[c]:
                c += 1
            q[1] = c
            if c not in u:
                u.append(c)
                a.append([q[0],q[1]])
        else:
            c += 1

    b = map(kulonb, a)
    b = list(b)

    print(*a[b.index(max(b))])
main()