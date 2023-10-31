def main():
    n = int(input())
    l = []
    for i in range(n):
        x,y = [int(j) for j in input().split()]
        l.append(y)
    print(l.index(max(l))+1)
main()