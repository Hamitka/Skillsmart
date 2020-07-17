def LineAnalysis(S):
    listPattern = list(S)
    if '.' not in listPattern:
        return True
    listPatternTemp = listPattern[1::]
    listOfListPattern = []
    y=0
    for i, item in enumerate(listPatternTemp):
       if item == '*':
           listOfListPattern += [listPatternTemp[y:i+1]]
           y=i+1
    setPattern = set(tuple(i) for i in listOfListPattern)
    if len(setPattern) <=1:
        return True
    else:
        return False

# s1 = '*..*..*..*..*..*..*'
# s2 = '*..*...*..*..*..*..*'
# s3 = '*..*..*..*..*..**..*'
# s4 = '*.......*.......*'
# s5 = '*.......*........*'
# s6 = '****'
#
# print(LineAnalysis(s1))
# print(LineAnalysis(s2))
# print(LineAnalysis(s3))
# print(LineAnalysis(s4))
# print(LineAnalysis(s5))
# print(LineAnalysis(s6))
