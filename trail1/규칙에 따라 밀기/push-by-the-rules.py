a = input()
way = input()

arr = list(way)

for i in range(len(way)):
    if arr[i] == 'L':
        a = a[1:] + a[0]
    elif arr[i] == 'R':
        a = a[-1] + a[:-1]

print(a)