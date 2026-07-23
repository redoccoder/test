n, m = map(int, input().split())

arr_2d = [[0] * n for _ in range(n)]

cnt = 1

for i in range(1, m + 1):
    r, c = tuple(map(int, input().split()))
    arr_2d[r - 1][c - 1] = i

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()