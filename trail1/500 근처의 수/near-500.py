a = list(map(int, input().split()))

max_val = 0
min_val = 1001

for i in a:
    if i < 500:
        if i > max_val:
            max_val = i
    elif i > 500:
        if i < min_val:
            min_val = i

print(max_val, min_val, end=" ")