n = int(input())

lst = []

for _ in range(n):
    lst.append(input())

a = input()

cnt = 0
sum = 0

for i in lst:
    if a[0] == i[0]:
        cnt += 1
        sum += len(i)

avg = sum / cnt

print(f"{cnt} {avg:.2f}", end=" ")