start, end = map(int, input().split())

answer_cnt = 0

for i in range(start, end + 1):
    cnt = 0
    for j in range(1, i + 1):
        if i % j == 0:
            cnt += 1
    if cnt == 3:
        answer_cnt += 1

print(answer_cnt)