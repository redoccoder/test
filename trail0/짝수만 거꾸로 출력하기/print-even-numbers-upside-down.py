N = int(input())
n = list(map(int, input().split()))

n.reverse()

for num in n:
    if num % 2 == 0:
        print(num, end = " ")