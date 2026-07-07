A1, A2 = map(int, input().split())

lst = [A1, A2]

sum = 0

for i in range(3, 11):
    sum = lst[-1] + lst[-2] * 2
    lst.append(sum)

print(*lst)