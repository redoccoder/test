lst = []

for _ in range(4):
    arr = list(map(int, input().split()))
    lst.append(arr)

total = 0

for i in range(4):
    for j in range(4):
        if i >= j:
            total += lst[i][j]

print(total)