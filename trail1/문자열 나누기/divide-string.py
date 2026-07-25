a = int(input())
b = input().split()

result = ""

for i in b:
    result += i

for i in range(0, len(result), 5):
    print(result[i : i+5])