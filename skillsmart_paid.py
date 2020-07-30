def SherlockValidString(s: str):
    lstCountS = [list(s).count(i) for i in set(list(s))]
    if len(set(lstCountS)) == 1:
        return True
    for i in range(len(lstCountS)):
        lstCountS[i] -= 1
        if 0 in lstCountS:
            if len(set(lstCountS[0:i] + lstCountS[i + 1:])) == 1: return True
        else:
            if len(set(lstCountS)) == 1: return True
        lstCountS[i] += 1
    return False


# print(SherlockValidString('xyz'))
# print(SherlockValidString('xxyyz'))
# print(SherlockValidString('xyzaa'))
# print(SherlockValidString('xxyyzabc'))
# print(SherlockValidString('xxyyza'))
# print(SherlockValidString('xyzzz'))
# print(SherlockValidString('xxxxyyyzzz'))
# print(SherlockValidString('x'))
# print(SherlockValidString('xy'))
