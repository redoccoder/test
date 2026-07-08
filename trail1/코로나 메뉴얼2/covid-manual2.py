lst = [0] * 4

for i in range(3):
    sym, temp = input().split()
    temp = int(temp)
    if sym == "Y" and temp >= 37:
        lst[0] += 1
    elif sym  == "N" and temp >= 37:
        lst[1] += 1
    elif sym == "Y" and temp < 37:
        lst[2] += 1
    elif sym == "N" and temp < 37:
        lst[3] += 1
    if lst[0] >= 2:
        lst.append("E")

print(*lst)