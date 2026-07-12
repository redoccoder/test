N = int(input())
arr = list(map(int, input().split()))

minVal = 101
sum = 0

for i in range(N - 1):
    sum = arr[i + 1] - arr[i]
    if sum < minVal:
        minVal = sum

print(minVal)