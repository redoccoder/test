a = input()

arr = list(a)

for i in range(len(a)):
    rem = int(input())
    
    if rem >= len(arr):
        arr.pop(-1)
    else:
        arr.pop(rem)

    print(''.join(arr))
    
    if len(arr) == 1:
        break