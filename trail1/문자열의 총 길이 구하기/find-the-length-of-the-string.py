a = input()

sum = 0

for i in a.split():
    sum += len(i)
    if i == " ":
        sum += 0

print(sum)