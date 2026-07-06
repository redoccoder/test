N = int(input())
arr = list(map(float, input().split()))

sum = 0
avg = 0

for i in arr:
    sum += i
    avg = sum / N

print(f"{avg:.1f}")

if avg >= 4:
    print("Perfect")
elif avg >= 3:
    print("Good")
else:
    print("Poor")