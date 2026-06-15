a = int(input())

for i in range(1, a + a, 2):
    for j in range(i):
        print("*", end="")
    print()