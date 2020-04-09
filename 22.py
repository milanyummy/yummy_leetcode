def generateParenthesis(n: int):
    ans = []
    def addNext(left, right, S):
        if right == 0:
            ans.append(''.join(S))
            return
        if left > 0:
            S.append('(')
            addNext(left-1, right, S)
            S.pop()
        if left < right:
            S.append(')')
            addNext(left, right-1, S)
            S.pop()
    addNext(n, n, [])
    return ans

n = 3
print( generateParenthesis(n) )
