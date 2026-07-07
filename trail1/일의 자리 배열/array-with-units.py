arr = list(map(int, input().split()))

for i in range(3, 11):
    next_num = (arr[-1] + arr[-2]) % 10
    arr.append(next_num)

for j in arr:
    print(j, end=" ")