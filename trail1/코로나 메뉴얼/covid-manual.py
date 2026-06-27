ch1, tmp1 = input().split()
ch2, tmp2 = input().split()
ch3, tmp3 = input().split()

tmp1 = int(tmp1)
tmp2 = int(tmp2)
tmp3 = int(tmp3)

cnt = 0

if ch1 == "Y" and tmp1 >= 37:
    cnt += 1
if ch2 == "Y" and tmp2 >= 37:
    cnt += 1
if ch3 == "Y" and tmp3 >= 37:
    cnt += 1
if cnt >= 2:
    print("E")
else:
    print("N")