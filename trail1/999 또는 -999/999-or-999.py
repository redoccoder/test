a = list(map(int, input().split()))

result = []

for i in a:
    if i == 999 or i == -999:
        break
    else:
        result.append(i)

print(max(result), min(result))