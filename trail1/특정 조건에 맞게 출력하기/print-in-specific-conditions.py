arr = list(map(int, input().split()))

lst = []

for i in arr:
    if i == 0:
        break
    if i % 2 == 1:
        lst.append(i + 3)
    else:
        lst.append(i // 2)

print(*lst)