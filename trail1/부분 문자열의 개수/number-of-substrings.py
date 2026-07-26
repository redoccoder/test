a = input()
b = input()

length = len(a)

target = b[0]

cnt = 0

for i in range(length - 1):
    if a[i: i + 2] == b:
        cnt += 1

print(cnt)