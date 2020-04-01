def lastRemaining(n: int, m: int) -> int:
    List1 = list(range(n))
    ptr = 0
    while (len(List1) > 1):
        ptr += (m-1)
        ptr = ptr%len(List1)
        List1.pop(ptr)
    return List1[0] 

x = lastRemaining(5, 3)

print(x)