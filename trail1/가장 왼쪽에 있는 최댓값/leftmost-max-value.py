n = int(input())
a = list(map(int, input().split()))

while n > 0:
    max_val = 0
    idx = 0
    for i in range(n):
        if a[i] > max_val:
            max_val = a[i]
            idx = i
    
    print(idx + 1, end=" ")

    n = idx