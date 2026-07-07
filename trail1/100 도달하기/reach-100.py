N = int(input())

lst = [1, N]

sum = 0

for i in range(1, 11):
    sum = lst[-1] + lst[-2]
    lst.append(sum)
    if sum > 100:
        break

print(*lst, end=" ")