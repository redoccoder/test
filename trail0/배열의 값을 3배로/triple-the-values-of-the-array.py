arr = []

for i in range(3):
    row = list(map(int, input().split()))
    new_row = []
    for j in row:
        new_row.append(j * 3)
    arr.append(new_row)

for row in arr:
    print(*row)