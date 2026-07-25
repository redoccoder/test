a = input()

target = a[0]
cnt = 0
result = ""

for i in a:
    if target == i:
        cnt += 1
    else:
        result += target + str(cnt)
        target = i
        cnt = 1

result += target + str(cnt)

print(len(result))
print(result)