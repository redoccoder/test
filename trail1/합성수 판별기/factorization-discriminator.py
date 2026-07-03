N = int(input())

sum = False
for i in range(2, N):
    if N % i == 0:
        sum = True

if sum == True:
    print("C")
else:
    print("N")