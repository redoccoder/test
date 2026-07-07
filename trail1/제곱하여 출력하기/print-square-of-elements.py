N = int(input())
arr = list(map(int, input().split()))

list = [i ** 2 for i in arr]

print(*list)