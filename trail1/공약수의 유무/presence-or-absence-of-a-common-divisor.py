A, B = map(int, input().split())

num = False
for i in range(A, B + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        num = True

if num == True:
    print(1) 
else:
    print(0)