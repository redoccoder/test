N = int(input())

sosu = False

for i in range(2, N):
    if N % i == 0:
        sosu = True

if sosu == True:
    print("C")
else:
    print("P")