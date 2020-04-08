words = ["hello","world","leetcode"]
chars = "welldonehoneyr"
length = 0
for word in words:
    charlist = chars
    for letter in word:
        charlist = charlist.replace(letter, "", 1)
    if len(chars) - len(charlist) == len(word):
        length += len(word)
    
print(length)