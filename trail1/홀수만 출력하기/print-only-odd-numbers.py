N = int(input())

i = 1

while i <= N:
    n = int(input())
    if n % 2 == 1 and n % 3 == 0:
        print(n)
    i += 1