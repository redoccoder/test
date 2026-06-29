A, B = map(int, input().split())

sum = 0

for i in range(A, B + 1):
    if i <= B:
        sum += i

print(sum)