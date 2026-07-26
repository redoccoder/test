a = input()
b = input()

length = len(a)
cnt = 0

for i in range(length):
    if a[i:i + len(b)] == b:
        cnt += i
        break

if b not in a:
    cnt = -1

print(cnt)