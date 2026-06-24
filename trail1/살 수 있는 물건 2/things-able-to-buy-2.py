N = int(input())

if N >= 3000:
    print("book")
elif 3000 > N >= 1000:
    print("mask")
elif 1000 > N >= 500:
    print("pen")
else:
    print("no")