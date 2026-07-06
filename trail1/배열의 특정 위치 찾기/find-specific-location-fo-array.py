a = list(map(int, input().split()))

sum_a = sum(a[1::2])
avg_a = sum(a[2::3]) / len(a[2::3])

print(f"{sum_a} {avg_a:.1f}")