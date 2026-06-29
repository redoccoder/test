N = int(input())

sum = 0

for i in range(N):
    n = int(input())
    if n % 2 == 1 and n % 3 == 0:
        sum += n

print(sum)