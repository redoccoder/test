A, B = map(int, input().split())

cnt_lst = [0] * 10

sum = 0

while A > 1:
    cnt_lst[A % B] += 1
    A //= B

for i in cnt_lst:
    sum += i ** 2

print(sum)