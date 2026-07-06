a = list(map(int, input().split()))

aa = []

for i in a:
    if i == 0:
        break
    else:
        aa.append(i)

print(*aa[::-1])