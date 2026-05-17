A, B, C = map(int, input().split())

if (A > B and A < C) or (A < B and A > C):
    print(A)
if (B > A and B < C) or (B < A and B > C):
    print(B)
if (C > A and C < B) or (C < A and C > B):
    print(C)