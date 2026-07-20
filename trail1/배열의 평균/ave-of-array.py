lst = []

for _ in range(2):
    arr = list(map(int, input().split()))
    lst.append(arr)
    
for i in lst:
    avg1 = sum(i) / 4
    print(f"{avg1:.1f}", end=" ")
print()

for j in range(4):
    avg2 = (lst[0][j] + lst[1][j]) / 2
    print(f"{avg2:.1f}", end=" ")
print()

total_avg = (sum(lst[0]) + sum(lst[1])) / 8
print(f"{total_avg:.1f}")