def TheRabbitsFoot(s, encode=False):
    def listTransponse(listIn):
        listOut = [[''] * len(listIn) for i in range(len(listIn))]
        for i in range(len(listIn)):
            for j in range(len(listIn[i])):
                try:
                    listOut[j][i] = listIn[i][j]
                except IndexError:
                    continue
        listOut = [''.join(i) for i in listOut]
        return listOut
    if encode == False:
        s = s.replace(' ', '')
        sqrtS = len(s)**.5
        upLimit = int(sqrtS+3/10+3/10+3/10 + 0.1)
        listMatrixS = [s[x:x+upLimit] for x in range(0, len(s), upLimit)]
        listCode = listTransponse(listMatrixS)
        return ' '.join(listCode)
    else:
        listDeCode = listTransponse(s.split())
        return ''.join(listDeCode)


# s = 'отдай мою кроличью лапку'
# scode = 'омоюу толл дюиа акчп йрьк'
# print(TheRabbitsFoot(s))
# print(TheRabbitsFoot(scode, True))