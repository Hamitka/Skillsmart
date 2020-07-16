def BigMinus(s1, s2):
    if s1 == s2:
        return '0'
    listS1 = [int(i) for i in s1[::-1]]
    listS2 = [int(i) for i in s2[::-1]]
    lenS1 = len(s1)
    lenS2 = len(s2)
    digitDiff = abs(lenS1-lenS2)
    if lenS1<lenS2:
        for i in range(digitDiff):
            listS1+=[0]
    elif lenS2<lenS1:
        for i in range(digitDiff):
            listS2+=[0]
    lenMax = len(listS1)
    for i in reversed(range(lenMax)):
        if listS1[i]<listS2[i]:
            listMax = listS2
            listMin = listS1
            break
        elif listS1[i]>listS2[i]:
            listMax = listS1
            listMin = listS2
            break
        else:
            continue

    listS3 = [(listMax[i]-listMin[i]) for i in range(lenMax)]
    for i in range(lenMax-1):
        if listS3[i] <0:
            listS3[i] = 10+listS3[i]
            listS3[i+1] = listS3[i+1]-1
    strList3 = ''.join([str(i) for i in listS3[::-1]])
    return strList3

# s2 = '510909421717094400000'
# s1 = '121645100408832000'
# # s2 = '12 1645 1004 0883 2000'
# s1_minus_s2 = '510787776616685568000'
#
# print(BigMinus(s1, s2))
# print(BigMinus('1', '321'))
# print(BigMinus('123456789', '123456789'))