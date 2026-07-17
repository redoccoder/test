n = int(input())

for i in range(n * 2):
    if i % 2 == 1:
        for i in range(n - (i - 1) // 2):
            print("*", end=" ")
        print()
    else:
        for i in range(1 + (i // 2)):
            print("*", end=" ")
        print()