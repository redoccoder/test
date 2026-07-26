a = input().split()

word1 = a[0]
word2 = list(a[1])

word2[0] = word1[0]
word2[1] = word1[1]

print(''.join(word2))