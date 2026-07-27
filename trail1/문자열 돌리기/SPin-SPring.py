l = input()

for i in range(len(l)):
    print(l)
    l = l[-1] + l[:len(l) - 1]

print(l)