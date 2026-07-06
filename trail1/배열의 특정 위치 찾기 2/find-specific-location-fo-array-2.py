arr = list(map(int, input().split()))

even_arr = sum(arr[1::2])
odd_arr = sum(arr[0::2])
sum = 0

if even_arr >= odd_arr:
    sum = even_arr - odd_arr
    print(sum)
else:
    sum = odd_arr - even_arr
    print(sum)