N = int(input())

cnt = 0

for i in range(N):
    exam = list(map(int, input().split()))
    total = sum(exam)
    avg = total / 4
    if avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)