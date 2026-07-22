n, m = map(int, input().split())

arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]

lst = []

for i in range(n):
    row_lst = []
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            row_lst.append(0)
        else:
            row_lst.append(1)
    lst.append(row_lst)

for row in lst:
    for elem in row:
        print(elem, end=" ")
    print()