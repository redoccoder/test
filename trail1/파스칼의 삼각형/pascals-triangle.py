n = int(input())

arr_2d = [[0] * n for _ in range(n)]

for i in range(n):
    arr_2d[i][0] = 1
    for j in range(1, i):
        arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]
    arr_2d[i][i] = 1

for i in range(n):
    for j in range(i + 1):
        print(arr_2d[i][j], end=" ")
    print()