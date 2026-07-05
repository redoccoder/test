a, b, c = map(int, input().split())

ble = False

for i in range(a, b + 1):
    if i % c == 0:
        ble = True

if ble == True:
    print("NO")
else:
    print("YES")