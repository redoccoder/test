a = int(input())

total = 0

for num in range(1, 101):
    total += num
    if total >= a:
        print(num)
        break