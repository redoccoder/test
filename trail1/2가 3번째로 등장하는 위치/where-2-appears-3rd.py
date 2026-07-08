N = int(input())
arr = list(map(int, input().split()))

cnt = 0
cnt2 = 0

for i in arr:
    cnt += 1
    if i == 2:
        cnt2 += 1
        if cnt2 == 3:
            print(cnt)
            break