n = 3
m = 3

arr1 = [list(map(int, input().split())) for _ in range(3)]
input()
arr2 = [list(map(int, input().split())) for _ in range(3)]

lst = []
total = 0

for i in range(3):
    row_lst = []
    for j in range(3):
        total = arr1[i][j] * arr2[i][j]
        row_lst.append(total)
    lst.append(row_lst)

for row in lst:
    for elem in row:
        print(elem, end=" ")
    print()