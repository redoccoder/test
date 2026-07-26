s, q = input().split()
q = int(q)

s = list(s)

for i in range(q):
    a = input().split()
    if a[0] == '1':
        idx1 = int(a[1]) - 1
        idx2 = int(a[2]) - 1
        s[idx1], s[idx2] = s[idx2], s[idx1]
    elif a[0] == '2':
        for j in range(len(s)):
            if s[j] == a[1]:
                s[j] = a[2]
    
    print(''.join(s))