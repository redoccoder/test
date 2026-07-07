arr = list(map(int, input().split()))

arr_cnt = [0] * 11

for i in arr:
    arr_cnt[i] += 1

for j in range(1, 7):
    print(f"{j} - {arr_cnt[j]}")