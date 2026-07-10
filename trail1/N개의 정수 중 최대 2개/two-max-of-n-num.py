n = int(input())
a = list(map(int, input().split()))

first = float('-inf')
second = float('-inf')

for i in a:
    if i >= first:
        second = first
        first = i
    elif i >= second:
        second = i

print(first, second)