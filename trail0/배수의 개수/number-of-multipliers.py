cnt1 = 0
cnt2 = 0

for num in range(10):
    num = int(input())
    if num % 3 == 0:
        cnt1 += 1
    if num % 5 == 0:
        cnt2 += 1

print(cnt1, cnt2, end=" ")