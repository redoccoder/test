A, B = map(int, input().split())

lst = [A, B]

for i in range(8):
    num = lst[-1] + lst[-2]
    lst.append(num % 10)

print(*lst)