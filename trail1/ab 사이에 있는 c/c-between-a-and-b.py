a, b, c = map(int, input().split())

rem = False
for i in range(a, b + 1):
    if i % c == 0:
        rem = True

if rem == True:
    print("YES")
else:
    print("NO")