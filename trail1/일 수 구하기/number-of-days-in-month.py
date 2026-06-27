month = int(input())

if month in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif month == 2:
    print(28)
else:
    print(30)