n = int(input())

for i in range(n):
    for j in range(1, i + 2):
        print(i * j + j, end=" ")
    print()