a, q = input().split()
q = int(q)

arr = list(a)

for i in range(q):
    req = input()
    if req == '1':
        a = a[1: len(a)] + a[0]
        print(a)
    elif req == '2':
        a = a[-1] + a[:len(a) - 1]
        print(a)
    elif req == '3':
        a = a[-1::-1]
        print(a)