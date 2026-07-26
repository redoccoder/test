a = input()

arr = list(a)

word1 = arr[0]
word2 = arr[1]

for i in range(len(arr)):
    if arr[i] == word1:
        arr[i] = word2
    elif arr[i] == word2:
        arr[i] = word1

print(''.join(arr))