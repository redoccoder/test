N = int(input())
arr = list(map(int, input().split()))

cnt = 0

for i, var in enumerate(arr):
    if var == 2:
        cnt += 1
        if cnt == 3:
            print(i + 1)
            break