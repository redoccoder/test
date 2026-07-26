a = input()

length = len(a)
cnt1 = 0
cnt2 = 0

for i in range(length - 1):
    if a[i:i + 2] == 'ee':
        cnt1 += 1
    elif a[i:i + 2] == 'eb':
        cnt2 += 1

print(cnt1, cnt2)