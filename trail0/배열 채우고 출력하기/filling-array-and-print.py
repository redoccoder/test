words = list(map(str, input().split()))

words.reverse()

for i in range(10):
    print(words[i], end="")
