N, Q = map(int, input().split())
N_arr = list(map(int, input().split()))

for i in range(Q):
    Q_arr = list(map(int, input().split()))

    if Q_arr[0] == 1:
        print(N_arr[Q_arr[1] - 1])
    elif Q_arr[0] == 2:
        if Q_arr[1] in N_arr:
            print(N_arr.index(Q_arr[1]) + 1)
        else:
            print(0)
    elif Q_arr[0] == 3:
        print(*N_arr[Q_arr[1] - 1 : Q_arr[2]])