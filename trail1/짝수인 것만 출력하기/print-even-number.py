N = int(input())
even_N = list(map(int, input().split()))

lst = []

for i in even_N:
    if i % 2 == 0:
        lst.append(i)

print(*lst)