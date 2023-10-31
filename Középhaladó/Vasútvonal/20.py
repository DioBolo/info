def main():
    n = int(input())
    l = []
    for i in range(n):
        x,y = [int(j) for j in input().split()]
        l.append(y-x)
    print(l.index(min(l))+1)
main()