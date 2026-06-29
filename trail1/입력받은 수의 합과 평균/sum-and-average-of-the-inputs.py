N = int(input())

sum = 0
cnt = 0

for i in range(N):
    n = int(input())
    sum += n
    cnt += 1

avg = sum / cnt
print(f"{sum} {avg:.1f}", end=" ")