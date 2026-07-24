lst = []

for _ in range(4):
    a = input()
    lst.append(a)

for row in lst[-1:-5:-1]:
    print(row)