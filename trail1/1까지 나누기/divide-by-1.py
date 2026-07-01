N = int(input())

cnt = 0

for i in range(1, N):
    if N <= 1:
        break
    else:
        N = N // i
        cnt += 1

print(cnt)