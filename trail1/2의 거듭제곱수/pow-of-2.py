N = int(input())

x = 0

while True:
    if N == 1:
        print(x)
        break
    else:
        N //= 2
        x += 1