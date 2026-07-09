N1, N2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(N1 - N2 + 1):
    if A[i : i + N2] == B:
        cnt += 1

if cnt == 1:
    print("Yes")
else:
    print("No")