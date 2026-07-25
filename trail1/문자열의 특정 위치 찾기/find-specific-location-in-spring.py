a = input().split()

target = a[1]

for i in range(len(a[0])):
    if target == a[0][i]:
        print(i)
        break

if target not in a[0]:
    print("No")