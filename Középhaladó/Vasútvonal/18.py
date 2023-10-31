def kulonb(l):
    return l[1] - l[0]
def main():
    n = int(input())
    u = [0]
    a = [[0,0]]
    q = [0,0]
    e = 0
    fl = [False]*(n+1)
    for i in range(1,n+1):
        x,y = [int(j) for j in input().split()]
        e += y-x
        if e != 0:
            fl[i] = True
    #print(fl)
    c = 0
    for k in fl:
        if k:
            q[0] = c
            while fl[c] and c<(len(fl)-1):
                c += 1
            q[1] = c
            if c not in u:
                u.append(c)
                a.append([q[0], q[1]])
        else:
            c += 1

    b = map(kulonb, a)
    b = list(b)

    print(*a[b.index(max(b))])

main()