N = int(input())

sosu = True

for i in range(2, N):
    if N % i == 0:
        sosu = False

if sosu == False:
    print("C")
else:
    print("P")