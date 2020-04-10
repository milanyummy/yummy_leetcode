def reverseWords(s):
    #调用内置API
    s1 = s.split()
    s1 = " ".join(s1[: : -1])
    return s1

s = "a good   example"
print (reverseWords( s ))