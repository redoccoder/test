n, m = map(int, input().split())

arr_2d = [[0] * n for _ in range(n)]

for i in range(1, m + 1):
    r, c = tuple(map(int, input().split()))
    arr_2d[r - 1][c - 1] = 1

for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()