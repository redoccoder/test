a = input()

lst = ["apple", "banana", "grape", "blueberry", "orange"]

cnt = 0

for i in range(5):
    if lst[i][2] == a or lst[i][3] == a:
        print(lst[i])
        cnt += 1

print(cnt)