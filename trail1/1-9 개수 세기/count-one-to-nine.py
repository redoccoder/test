N = int(input())
arr = list(map(int, input().split()))

cnt_arr = [0] * 10

for i in arr:
    cnt_arr[i] += 1

for j in range(1, 10):
    cnt = cnt_arr[j]
    print(cnt)