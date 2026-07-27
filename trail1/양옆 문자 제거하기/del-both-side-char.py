a = input()

arr = list(a)
arr.pop(1)
arr.pop(-2)

a = ''.join(arr)

print(a)