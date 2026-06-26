A, a = map(int, input().split())
B, b = map(int, input().split())

if A > B:
    print("A")
elif B > A:
    print("B")
elif A == B and a > b:
    print("A")
else:
    print("B")