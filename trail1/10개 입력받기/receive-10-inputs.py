a = list(map(int, input().split()))

sum = 0
cnt = 0

for i in a:
    if i == 0:
        break
    sum += i
    cnt += 1

avg = sum / cnt

print(f"{sum} {avg:.1f}")