gender = int(input())
age = int(input())

man = 0
woman = 1

if gender == 0:
    if age >= 19:
        print("MAN")
    else:
        print("BOY")

if gender == 1:
    if age >= 19:
        print("WOMAN")
    else:
        print("GIRL")