n = int(input())
nums = list(map(int, input().split()))

idx = -1
cnt = 0

for i in nums:
    if nums.count(i) == 1:
        if i > idx:
            idx = i

print(idx)