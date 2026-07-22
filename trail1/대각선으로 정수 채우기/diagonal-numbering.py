n, m = map(int, input().split())

arr_2d = [[0 for _ in range(m)] for _ in range(n)]

num = 1

for s in range(0, (n - 1) + (m - 1) + 1):
    for i in range(n):
        for j in range(m):
            if i + j == s:
                arr_2d[i][j] = num
                num += 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()