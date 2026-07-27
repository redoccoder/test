a = input()
b = input()

arr = list(a)

while b in ''.join(arr):
    for i in range(len(a)):
        if ''.join(arr[i: i + len(b)]) == b:
            for j in range(len(b)):
                arr.pop(i)
            break

print(''.join(arr))