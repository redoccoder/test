A, B = map(int, input().split())

print(f"{A // B}.", end="")

A = (A % B) * 10

for i in range(20):
    print(A // B, end="")
    A = (A % B) * 10