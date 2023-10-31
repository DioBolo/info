def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    max_length = -1
    max_indices = (-1, -1)
    current_start = 0
    current_sum = 0

    for i in range(n):
        current_sum += a[i][1] - a[i][0]
        while current_sum >= m:
            if i - current_start > max_length:
                max_length = i - current_start
                max_indices = (current_start + 1, i + 1)
            current_sum -= a[current_start][1] - a[current_start][0]
            current_start += 1

    print(*max_indices)


if __name__ == "__main":
    main()