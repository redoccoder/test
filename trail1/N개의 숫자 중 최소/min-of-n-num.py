n = int(input())
a = list(map(int, input().split()))

min_val = a[0]
cnt = 0

for i in a:
    if min_val > i:
        min_val = i

for j in a:
    if j == min_val:
        cnt += 1
        
print(min_val, cnt)