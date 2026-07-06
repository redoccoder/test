N = int(input())
arr = list(map(int, input().split()))

arrr = []

for i in arr:
    if i % 2 == 0:
        arrr.append(i)

print(*arrr[::-1])