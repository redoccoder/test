a = input()

arr = list(a)

for i in range((len(a))):
    if arr[i] == 'e':
        arr.pop(i)
        break

print(''.join(arr))