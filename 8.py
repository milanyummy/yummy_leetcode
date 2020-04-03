import re
def myAtoi(s) -> int:
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1
    s1 = s.strip()
    s1 = re.split('[ .]', s1)
    matchNum = re.match(r'^(\+|\-)?[0-9]+', s1[0])
    if matchNum == None:
        return 0
    result = int(matchNum.group(0))
    if result >  INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN
    return result


s = "  -0012a42"
print( myAtoi(s))
