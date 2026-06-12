a = input()

arr = list(a)

arr[1] = "a"
arr[-2] = "a"

print("".join(arr))