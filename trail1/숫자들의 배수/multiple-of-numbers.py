n = int(input())

lst = []

cnt = 0

for i in range(1, 11):
    lst.append(n * i)
    if (n * i) % 5 == 0:
        cnt += 1
        if cnt == 2:
            break

print(*lst)