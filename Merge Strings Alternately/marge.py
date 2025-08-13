word1 = "abse"
word2 = "pqrs"

marge = ""

i = 0
while i < len(word1) and i < len(word2):
    marge += word1[i] + word2[i]
    i += 1

print(marge)
